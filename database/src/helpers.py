#!/usr/env python
import json

def json_read(path):
  """ Read a json file from disk using json.load """
  with open(path, encoding="utf-8") as fp:
    return json.load(fp)

def json_write(path, obj):
  """ Write a json file to disk using json.dump """
  with open(path, "w", encoding='utf-8') as fp:
    json.dump(obj, fp, indent=4)

