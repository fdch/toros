#!/usr/env python
import glob
import json
from helpers import json_read, json_write
import config

tables = {}

for filepath in glob.glob(config.data_path + "/*.json"):
  name = filepath.split('/')[-1].split('.')[0]
  
  if filepath == config.tables_path:
    continue

  tables[name] = {
    "path" : filepath,
  }

if config.tables != tables:
  print("Writing new tables")
  json_write(config.tables_path, tables)
else:
  print("Tables already updated")
