#!/usr/env python

class Status:
  def __init__(self):
    self.NOT_FOUND = -2
    self.INITIAL = -1
    self.BEGIN_TRANSFER = 1
    self.END_TRANSFER = 0
    self.current = self.INITIAL

  def check(self, num):
    return self.current == num

  def get_status(self, num):
    return self.current
  
  def get_status_name(self):
    return self.get_name(self.current)

  def get_name(self, num):
    if num == -2:
      return "NOT_FOUND"
    elif num == 0:
      return "END_TRANSFER"
    elif num == 1:
      return "BEGIN_TRANSFER"
    else: # INITIAL == -1
      return "INITIAL"

  def get_code(self, string):
    if string == "NOT_FOUND":
      return -2
    elif string == "END_TRANSFER":
      return 0
    elif string == "BEGIN_TRANSFER":
      return 1
    else: # INITIAL
      return -1

  def set_status(self, num):
    if num == -2:
      self.current = self.NOT_FOUND
    elif num == 0:
      self.current = self.END_TRANSFER
    elif num == 1:
      self.current = self.BEGIN_TRANSFER
    else: # INITIAL == -1
      self.current = self.INITIAL

  def set_status_by_name(self, string):
    self.set_status(self.get_code(string))
   
