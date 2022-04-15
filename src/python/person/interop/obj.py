from typing import List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Person:
    Name:str = None
    Title:str = None
    Company:str = None
    Phone:str = None
    DOB:datetime = None

    def __init__(self, data:List):
        self.Company=data[0]
        self.DOB=data[1]
        self.Name=data[2]
        self.Phone=data[3]
        self.Title=data[4]