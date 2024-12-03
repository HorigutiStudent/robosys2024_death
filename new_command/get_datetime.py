#!/usr/bin/python3

# Copyright (c) 2024 Horiguchi Masahumi
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

from datetime import datetime

class GetDateTime:
  def __init__(self,):
    """日時情報を得る"""
    self.current_d = datetime.now()
    
  def get_month(self)->int:
    return self.current_d.month
  
  def get_week(self)->int:
    return (self.current_d.day - 1) // 7 + 1
  
  def get_day(self)->int:
    return self.current_d.day