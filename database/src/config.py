#!/usr/env python

from helpers import json_read

data_base = ".."
data_path = data_base + "/data"
tables_path = data_path + "/.tables.json"
tables = json_read(tables_path)
host = "127.0.0.1"
port = 9226
