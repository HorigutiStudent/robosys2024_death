#!/usr/bin/python3

# Copyright (c) 2024 Horiguchi Masahumi
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

import sys

class ParceInputData:
    def __init__(self,):
        self.input_data = ""

  
    def get_data(self) -> str:
        self.input_data = sys.stdin.read().strip()
        return self.input_data

  
    def to_num(self,type:str="int") -> list:
        inputs = []
        for num in self.input_data:
            if type == "int":
                inputs.append(int(num))
            elif type == "float":
                inputs.append(float(num))
            else:
                raise KeyError(f"the type {type} is unexpected")
        return inputs