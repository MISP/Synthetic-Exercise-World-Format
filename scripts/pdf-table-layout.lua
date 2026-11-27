-- Link targets make image cells wide in Markdown. Size the two image tables
-- by their contents on paper so neighboring text columns stay readable.
local image_tables = {
  ['Map or diagram'] = {0.42, 0.58},
  ['Flag'] = {0.22, 0.21, 0.17, 0.40},
}

function Table(table)
  local header = table.head.rows[1]
  if not header then return end
  local first_cell = header.cells[1]
  if not first_cell then return end
  local widths = image_tables[pandoc.utils.stringify(first_cell.contents)]
  local columns = table.colspecs
  if not widths or #widths ~= #columns then return end
  for index, width in ipairs(widths) do
    columns[index][2] = width
  end
  table.colspecs = columns
  return table
end
