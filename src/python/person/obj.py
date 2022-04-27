from dataclasses import dataclass
from datetime import datetime

@dataclass
class Person:
    name:str = None
    title:str = None
    company:str = None
    phone:str = None
    dob:datetime = None
