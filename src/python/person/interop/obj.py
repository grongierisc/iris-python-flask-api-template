from typing import List
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from decimal import Decimal

@dataclass
class Person:
    nameBytes:bytes = None
    titleDecimal:Decimal = None
    companyUUID:UUID = None
    phone:str = None
    dob:datetime = None
