#!/usr/env python
import json

def json_load(path):
  with open(path, encoding="utf-8") as f:
    return json.load(f)


