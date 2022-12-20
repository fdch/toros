#!/usr/env python
import json
from helpers import json_read
from types import SimpleNamespace
import config as _config
import socket
import pickle
from status import Status
#from logger import logger

class DBClient(object):
  def __init__(self):
    # the name of the database
    self.tables_path = _config.tables_path
    # the json object hook
    self.hook = lambda d: SimpleNamespace(**d) 
    # load the database
    self.load_db()
    # the connection
    self.conn = None  
    # host and port for the socket server
    self.host = _config.host
    self.port = _config.port
    self.addr = None # the address of the client
    # Start the socket server
    self.status = Status()
   
    self.host = _config.host
    self.port = _config.port
    self.chunk_count = 0
    self.data_chunks = bytearray()
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.status = Status()
  


  def to_pickle(self, data):
    return pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)

  def send_pickle(self, obj):
    self.conn.sendall(self.to_pickle(obj))
   
  def report_status(self, name):
    self.status.set_status_by_name(name)
    self.send_pickle(self.status)
  
  def send_object(self, obj):
    print("Begin sending packet")
    self.report_status("BEGIN_TRANSFER")
    
    p_obj = self.to_pickle(obj)
    p_obj_list = memoryview(p_obj).tolist()
    print(f"Packet size {len(p_obj_list)}")
    print("Sending packets...")
    
    while len(p_obj_list):
      self.packets += 1
      print(f"packet {self.packets}")
      start = len(p_obj_list) - 4096
      print(f"start point: {start}")
      if start >= 0:
        packet = p_obj_list[:start]
        p_obj_list = p_obj_list[start:]
      else:
        packet = p_obj_list
        p_obj_list = []
      print("sending",packet)
      self.send_pickle(packet)
    
    print(f"End sending {self.packets} packets.")
    self.packets = 0
    self.report_status("END_TRANSFER")


  def connect_loop(self):
    while self.keep_alive:
      conn_loop = 0
      print(f"Listening on {self.host}:{self.port}")
      self.conn, addr = self.sock.accept()
    
      print(f"Connected by {addr}")
      while True:
        print(f"starting connection: {conn_loop}")
        self.report_status("INITIAL")
        
        data = self.conn.recv(1024)
        
        if not data: break
        
        query = data.decode('utf-8')
        print("client says:", query)
        print(dir(self)) 
        if query not in dir(self):
          print("not found")
          #self.report_status("NOT_FOUND")
          pass
        else:
          self.conn.sendall(self.to_pickle(getattr(self,query)))
          #self.send_object(getattr(self, query))
          print("Finished transfer.")
        
        conn_loop += 1

      self.conn.close()


  def load_db(self):
    #print("loading db", self.tables_path)
    if not self.tables_path:
      print("No database tables path provided. Update ``self.tables_path``")
      return
    tables = json_read(self.tables_path, object_hook = self.hook)
    #print("TABLES",tables)
    setattr(self, 'tables', tables)
    #print(tables, self.tables_path, self.tables) 
    for table_name, table_path in self.tables.__dict__.items():
      print(f"Loading table {table_name}")
      setattr(self, table_name, json_read(table_path.path, object_hook = self.hook))
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


