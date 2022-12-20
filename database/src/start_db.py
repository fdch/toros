#!/usr/env python
import schemas
import config
import json
from server import Server

if __name__ == "__main__":
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('-host',  type=str, default="127.0.0.1")
  parser.add_argument('-port',  type=int, default=9226)
  args = parser.parse_args()
  db = Server()
