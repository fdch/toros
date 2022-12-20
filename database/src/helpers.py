#!/usr/env python
import json

def json_read(path, **kwargs):
  """ Read a json file from disk using json.load """
  with open(path, encoding="utf-8") as fp:
    return json.load(fp, **kwargs)

def json_write(path, obj, indent=4, **kwargs):
  """ Write a json file to disk using json.dump """
  with open(path, "w", encoding='utf-8') as fp:
    json.dump(obj, fp, indent=indent)


def json_from_namespace(obj, indent=4):
  """ Return a JSON representation of the obj's scope as a string """

  # inner function to filter out variables that are
  # prefixed with two underscores ('_') 
  # with the exception of '__pdpy__'
  def __filter__(o):
    return { 
      k : v 
      for k,v in o.__dict__.items() 
      if not k.startswith("__")
    }

  return json.dumps(
    obj,
    default   = __filter__,
    sort_keys = False,
    indent    = indent
  )

