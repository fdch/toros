#!/usr/env python
import glob
import json
from helpers import json_load

base = ".."
tables_path = base + "/tables.json"
path = base + "/data"
schema = base + "/schemas"
tables = {}

for filepath in glob.glob(path + "/*.json"):
  name = filepath.split('/')[-1].split('.')[0]
  schemapath =  schema + "/" + name + ".schema.json"

  try:
    schema_file = json_load(schemapath)
  except Exception as e:
    print(f"ERROR loading table {name} with path {filepath}")
    print("Possibly, the schema file is missing")
    print(e)
    quit()

  tables[name] = {
    "path" : filepath,
    "schema" : schemapath
  }

with open(tables_path, "w", encoding='utf-8') as f:
  f.write(json.dumps(tables, indent=4))
