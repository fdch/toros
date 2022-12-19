#!/usr/env python

import json
from helpers import json_read

tables_path = './tables.json'

tables = json_read(tables_path)

db = {}

for (table_name, table_paths) in tables.items():
  # print(table_name, table_path)
  db[table_name] = json_read(table_paths['path'])

print(json.dumps(db, indent=4))
