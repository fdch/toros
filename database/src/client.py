#!/usr/env python3

import socket
import json
import pickle
import config as _config
from helpers import json_from_namespace
from status import Status
#from logger import logger

class Client(object):
  def __init__(self):
    
    self.host = _config.host
    self.port = _config.port
    self.chunk_count = 0
    self.data_chunks = bytearray()
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.status = Status()
  

  def handle_response(self, response):
    data = pickle.loads(response)
    print("DATA",data)
   # if isinstance(data, Status):
   #   # status object
   #   print("STATUS:", self.status.get_status_name())
   #   self.status = data

   #   if self.status.check(-2):
   #     print(f"Querying '{x}' returned empty")
   #   elif self.status.check(-1): # self.status.check(-1) == "INITIAL"
   #     print("Initial state")
   #   else:
   #     print("Wrong status")
   #     return 1

   # else: # incoming data ...
   #   print("Incoming data ...")
   #   if self.status.check(1):
   #     self.chunk_count += 1
   #     print(f"... appending chunk #{self.chunk_count}...: {data}")
   #     self.data_chunks += data
   #   elif self.status.check(0):
   #     print(f"... finished {self.chunk_count} chunks.")
   #     self.chunk_count = 0
   #     data = self.data_chunks
   #     self.data_chunks = bytearray()
   #     #data = json_from_namespace(data)
   #     print("Received data:", data)
   
  def disconnect(self):
    """ Disconnect from the socket server"""
    print("Disconnecting")
    self.sock.close()

  def connect(self):
    """ Connect to the socket server """
    print("Connecting to host")
    self.sock.connect((self.host, self.port))

  def receive(self, callback):
    """ Receive data from socket"""
    print("Receiving data")
    response = b''
    data = True
    while data:
      data = self.sock.recv(1024)
      response += data
    callback(response)
    
  def send(self, command, callback):
    """ Send data to socket passing a callback"""

    print("Sending", command)
    self.sock.sendall(command)
    self.receive(callback)
   
  def query(self):
    """ Query the database """
    self.connect()

    print("Type QUIT or EXIT to exit terminal")
    while True:
      x = input("Query the database: ")
      if x == 'quit()' or x == 'QUIT' or x == 'EXIT':
        break 
    
      # send query
      #self.send(x.encode('utf-8'), self.handle_response)
      self.sock.sendall(x.encode('utf-8'))
      resp = b''
      resp += self.sock.recv(1024)
      
      print(resp)
    
    self.disconnect()


