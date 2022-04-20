from typing import List
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from decimal import Decimal

@dataclass
class Person:
    name:str = None
    title:str = None
    company:str = None
    phone:str = None
    dob:datetime = None
