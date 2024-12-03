#!/usr/bin/python3

# Copyright (c) 2024 Horiguchi Masahumi
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

import sys
sys.path.append("/home/RoboSys/robosys2024")

from new_command.parce_input_data import ParceInputData
import re


class GetPlaceInfo:
    def __init__(self,):
        self.parce_input_data = ParceInputData()
    
    
    def done(self) -> str:
        input_data = self.parce_input_data.get_data()
        return self.__get_place(input_data)
    
    
    def __get_place(self,input_data:str) -> str:
        if input_data[0] == "t":#入力の頭文字が津田沼のtなら
            return "td"
        elif input_data[0] == "s":#入力の頭文字が新習志野のsなら
            return self.__get_floor(input_data)
        else:
            raise KeyError(f"the input option {input_data} is unexpected")
    
    
    def __get_floor(self,input_data:str) -> str:
        """新習志野校舎のみ何階かの情報が必要"""
        m = re.search(r'\d+$',input_data).group()
        if len(m) != 1:
            raise KeyError(f"floor info is not match correct pattern {input_data}")
        if m == "1":
            return "sd1"
        else:
            return "sd2"