#!/usr/env python

import json
from helpers import json_load

tables_path = './tables.json'

tables = json_load(tables_path)

db = {}

for (table_name, table_paths) in tables.items():
  # print(table_name, table_path)
  db[table_name] = json_load(table_paths['path'])

print(json.dumps(db, indent=4))
