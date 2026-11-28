#!/usr/bin/env python3
"""Build the Synthetic Exercise World PDF from the repository's Markdown guides."""

import argparse
import html
import json
import posixpath
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/MISP/Synthetic-Exercise-World-Format"
RAW_IMAGES = "https://raw.githubusercontent.com/MISP/Synthetic-Exercise-World-Format/refs/heads/main/"
MISP_BOOK_REVISION = "b675fdc9e3926490bd104a3280e2344c10269b8f"
MISP_BOOK_SOURCE = f"https://raw.githubusercontent.com/MISP/misp-book/{MISP_BOOK_REVISION}"
PDF_NAME = "synthetic-exercise-world.pdf"
PANDOC_READER = "markdown+gfm_auto_identifiers+autolink_bare_uris-blank_before_header"

# GitHub's HTML thumbnails need native Pandoc image nodes for Typst.
THUMBNAIL = re.compile(
    r'<a href="([^"]+)"><img src="([^"]+)" alt="([^"]*)" width="(\d+)"'
    r'(?: height="(\d+)")?\s*/?></a>'
)
GUIDE_LINK = re.compile(r"\]\((extensions/[^/()\s]+/README\.md)(?:#[^)]*)?\)")


def native_thumbnail(match):
    href, source, alt, width, height = map(lambda value: html.unescape(value or ""), match.groups())
    alt = alt.replace("\\", "\\\\").replace("[", r"\[").replace("]", r"\]")
    dimensions = f"width={float(width) * 25.4 / 96:.2f}mm"
    if height:
        dimensions += f" height={float(height) * 25.4 / 96:.2f}mm"
    return f"[![{alt}](<{source}>){{{dimensions}}}](<{href}>)"


def pandoc(source, from_format, to_format):
    return subprocess.run(
        ["quarto", "pandoc", "--from", from_format, "--to", to_format, "--wrap=none"],
        input=source, text=True, encoding="utf-8", check=True, stdout=subprocess.PIPE,
    ).stdout


def nodes(tree):
    if isinstance(tree, dict):
        if "t" in tree:
            # Some Pandoc nodes are enums with no content.
            yield tree
        for value in tree.values():
            yield from nodes(value)
    elif isinstance(tree, list):
        for item in tree:
            yield from nodes(item)


def prepare_chapters(work, readme, revision):
    source_root = "README.md"
    atlas = "geography/README.md"
    exercise = "misp-exercise/README.md"
    acknowledgements = "acknowledgements/README.md"
    available = {path.relative_to(ROOT).as_posix() for path in (ROOT / "extensions").glob("*/README.md")}
    ordered = dict.fromkeys(GUIDE_LINK.findall(readme))
    guides = [*ordered, *sorted(available - ordered.keys())]
    chapters = {
        source_root: "index",
        atlas: "geographic-atlas",
        exercise: "misp-exercise",
        **{guide: f'extension-{Path(guide).parent.name}' for guide in guides},
        acknowledgements: "acknowledgements",
    }
    documents = {}
    section_ids = {}
    for source, slug in chapters.items():
        markdown = readme if source == source_root else (ROOT / source).read_text(encoding="utf-8")
        document = json.loads(pandoc(THUMBNAIL.sub(native_thumbnail, markdown), PANDOC_READER, "json"))
        headers = [node for node in nodes(document) if node["t"] == "Header"]
        if not headers or headers[0]["c"][0] != 1:
            raise ValueError(f"{source} needs a level-one title")
        for index, header in enumerate(headers):
            attributes = header["c"][1]
            original = attributes[0]
            identifier = slug if index == 0 else f"{slug}-{original}"
            section_ids[source, original] = identifier
            attributes[0] = identifier
        if source == source_root:
            headers[0]["c"][2] = [
                {"t": "Str", "c": "Project"}, {"t": "Space"}, {"t": "Str", "c": "overview"},
            ]
        documents[source] = document

    def resolve(source, target, image):
        if target.startswith(RAW_IMAGES):
            target = "/" + target.removeprefix(RAW_IMAGES)
        url = urlsplit(target)
        if url.scheme or url.netloc:
            return target
        path = unquote(url.path)
        if path.startswith("/"):
            path = path.lstrip("/")
        else:
            path = posixpath.join(posixpath.dirname(source), path) if path else source
        path = posixpath.normpath(path)
        resource = ROOT / path
        if not resource.is_file() or not resource.resolve().is_relative_to(ROOT):
            raise ValueError(f"{source} links to missing repository file {target}")
        if image:
            destination = work / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            if not destination.exists():
                shutil.copyfile(resource, destination)
            return path
        if path in chapters:
            identifier = section_ids.get((path, unquote(url.fragment))) if url.fragment else chapters[path]
            if not identifier:
                raise ValueError(f"{source} links to missing section {target}")
            return f"#{identifier}"
        fragment = f"#{url.fragment}" if url.fragment else ""
        query = f"?{url.query}" if url.query else ""
        return f"{REPOSITORY}/blob/{quote(revision, safe='')}/{quote(path, safe='/')}{query}{fragment}"

    for source, slug in chapters.items():
        document = documents[source]
        for node in nodes(document):
            kind = node["t"]
            if kind in {"Image", "Link"}:
                target = node["c"][2]
                target[0] = resolve(source, target[0], image=kind == "Image")
            elif kind == "RawInline" and node["c"] in (["html", "<br>"], ["html", "<br/>"], ["html", "<br />"]):
                node["t"] = "Space"
                del node["c"]
        (work / f"{slug}.qmd").write_text(
            pandoc(json.dumps(document), "json", "markdown"), encoding="utf-8",
        )
    return [
        "index.qmd",
        "geographic-atlas.qmd",
        "misp-exercise.qmd",
        {"part": "World extensions", "chapters": [f"{chapters[guide]}.qmd" for guide in guides]},
        "acknowledgements.qmd",
    ]


def stage_template(work):
    fonts = [
        "SourceSans3-Regular.otf", "SourceSans3-Semibold.otf", "SourceSans3-Bold.otf",
        "SourceSans3-It.otf", "SourceCodePro-Regular.otf", "SourceCodePro-Semibold.otf",
        "source-sans-LICENSE.md", "source-code-pro-LICENSE.md",
    ]
    assets = [
        "assets/misp-2-verti.png", "assets/pdf/misp-book.typ",
        "assets/pdf/typst-show.typ", "assets/pdf/pdf-layout.lua",
        *(f"assets/pdf/fonts/{font}" for font in fonts),
    ]
    print(f"Loading the MISP Book template at {MISP_BOOK_REVISION[:7]}", flush=True)
    for asset in assets:
        destination = work / asset
        destination.parent.mkdir(parents=True, exist_ok=True)
        with urlopen(f"{MISP_BOOK_SOURCE}/{asset}", timeout=30) as response:
            destination.write_bytes(response.read())

    # Reuse the layout, palette, logo and fonts. Give the running text and cover
    # link this book's identity.
    template = work / "assets/pdf/misp-book.typ"
    text = template.read_text(encoding="utf-8")
    for old, new in {
        "MISP USER GUIDE": "SYNTHETIC EXERCISE WORLD",
        "MISP Intelligence Sharing Platform": "Synthetic Exercise World",
        "USER DOCUMENTATION": "WORLD DOCUMENTATION",
        'link("https://www.misp-project.org")[www.misp-project.org]':
            f'link("{REPOSITORY}")[Synthetic Exercise World on GitHub]',
    }.items():
        if old not in text:
            raise ValueError(f"The pinned MISP Book template lacks {old!r}")
        text = text.replace(old, new)
    template.write_text(text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_book" / PDF_NAME,
                        help="PDF path (default: _book/synthetic-exercise-world.pdf)")
    parser.add_argument("--revision", default="main",
                        help="GitHub source revision used for links to repository files")
    args = parser.parse_args()
    if not shutil.which("quarto"):
        parser.error("Quarto 1.9.38 must be installed and on PATH")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    title, _, subtitle = readme.splitlines()[0].removeprefix("# ").partition(" - ")

    with tempfile.TemporaryDirectory(prefix="sewf-quarto-") as temp:
        work = Path(temp)
        chapters = prepare_chapters(work, readme, args.revision)
        stage_template(work)
        shutil.copyfile(ROOT / "scripts" / "pdf-table-layout.lua", work / "pdf-table-layout.lua")
        config = {
            "project": {"type": "book", "output-dir": "_book"},
            "book": {
                "title": title, "subtitle": subtitle, "author": "The MISP Project & Contributors",
                "date": "today", "output-file": Path(PDF_NAME).stem, "chapters": chapters,
            },
            "execute": {"enabled": False},
            "format": {"typst": {
                "papersize": "a4", "toc": True, "toc-depth": 1, "number-sections": False,
                "fontsize": "10.5pt", "mainfont": "Source Sans 3", "codefont": "Source Code Pro",
                "font-paths": ["assets/pdf/fonts"],
                "template-partials": ["assets/pdf/typst-show.typ"],
                "filters": [
                    {"path": "assets/pdf/pdf-layout.lua", "at": "post-quarto"},
                    {"path": "pdf-table-layout.lua", "at": "post-quarto"},
                ],
            }},
        }
        # JSON is also valid YAML.
        (work / "_quarto.yml").write_text(json.dumps(config, indent=2), encoding="utf-8")
        subprocess.run(["quarto", "render", "--to", "typst"], cwd=work, check=True)
        generated = work / "_book" / PDF_NAME
        args.output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(generated, args.output)
    print(f"PDF written to {args.output.resolve()}")


if __name__ == "__main__":
    main()
