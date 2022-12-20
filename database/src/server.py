#!/usr/env python
import json
from helpers import json_read
from types import SimpleNamespace
import config as _config
import socket
import pickle
from status import Status

class Server(object):
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
    self.listen()
    # keep the server alive
    self.keep_alive = True
    self.packets = 0
    self.status = Status()
    self.conn = None
    # Start the connections
    self.connect_loop()

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
        
        if query not in dir(self):
          self.report_status("NOT_FOUND")
        else:
          self.send_object(getattr(self, query))
          print("Finished transfer.")
        
        conn_loop += 1

      self.conn.close()

  def __setattr__(self, name, value):
    """ Hijack setattr to return ourselves as a dictionary """
    if value is not None:
      self.__dict__[name] = value
 
  def load_db(self):
    if not self.tables_path:
      print("No database tables path provided. Uptade ``self.tables_path``")
      return

    setattr(self, 'tables', json_read(self.tables_path, object_hook = self.hook))
     
    for table_name, table_path in self.tables.__dict__.items():
      print(f"Loading table {table_name}")
      setattr(self, table_name, json_read(table_path.path, object_hook = self.hook))

  def listen(self):
    """ Start the socket server """
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.sock.bind((self.host, self.port))
    self.sock.listen()
   
  def __json__(self, indent=4):
    """ Return a JSON representation of the instance's scope as a string """

    def __filter__(o):
      return { 
        k : v 
        for k,v in o.__dict__.items() 
      }

    return json.dumps(
      self,
      default   = __filter__,
      sort_keys = False,
      indent    = indent
    )
 
