#!/usr/env python3

import socket
import json
import pickle
import config as _config
from helpers import json_from_namespace
from status import Status

class Client(object):
  def __init__(self):
    
    self.host = _config.host
    self.port = _config.port
    self.chunk_count = 0
    self.data_chunks = bytearray()
    self.sock = None
    self.status = Status()
  

  def handle_response(self, response):
    data = pickle.loads(response)
    if isinstance(data, Status):
      # status object
      print("STATUS:", self.status.get_status_name())
      self.status = data

      if self.status.check(-2):
        print(f"Querying '{x}' returned empty")
      elif self.status.check(-1): # self.status.check(-1) == "INITIAL"
        print("Initial state")
      else:
        print("Wrong status")
        return 1

    else: # incoming data ...
      print("Incoming data ...")
      if self.status.check(1):
        self.chunk_count += 1
        print(f"... appending chunk #{self.chunk_count}...: {data}")
        self.data_chunks += data
      elif self.status.check(0):
        print(f"... finished {self.chunk_count} chunks.")
        self.chunk_count = 0
        data = self.data_chunks
        self.data_chunks = bytearray()
        #data = json_from_namespace(data)
        print("Received data:", data)
   
  def connect(self):
    """ Connect to the socket server """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting to host")
    sock.connect((self.host, self.port))
    return sock

  def send(self, command):
    sock = self.connect()
    response = bytearray()
    data = True
    print("Sending", command)
    sock.sendall(command)
    while data:
      data = sock.recv(1024)
      response += data
        
    sock.close()
    return response

  def query(self):
    print("Type QUIT or EXIT to exit terminal")
  
    x = input("Query the database: ")
    if x == 'quit()' or x == 'QUIT' or x == 'EXIT':
      return 1 
    
    # send query
    response = self.send(x.encode('utf-8'))

    return self.handle_response(response)

