from dataclasses import dataclass
from datetime import date

@dataclass
class Person:
    name:str = None
    title:str = None
    company:str = None
    phone:str = None
    dob:date = None
