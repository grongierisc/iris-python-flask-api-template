from dataclasses import dataclass
import grongier.pex
from typing import List
from interop.obj.ClassPerson import Person

@dataclass
class GetAllPersonResponse(grongier.pex.Message):

    Persons:List[Person] = None

@dataclass
class GetAllPersonResquest(grongier.pex.Message):

    currPage:int=None
    pageSize:int=None