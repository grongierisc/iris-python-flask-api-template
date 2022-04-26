from dataclasses import dataclass
from typing import List
from grongier.pex import Message
from interop.obj import Person

@dataclass
class CreatePersonRequest(Message):

    person:Person = None

@dataclass
class CreatePersonResponse(Message):

    id:int=None

@dataclass
class GetAllPersonResponse(Message):

    persons:List[Person] = None

@dataclass
class GetAllPersonRequest(Message):

    currPage:int=None
    pageSize:int=None

@dataclass
class GetPersonResponse(Message):

    person:Person = None

@dataclass
class GetPersonRequest(Message):

    id:int = None

@dataclass
class UpdatePersonRequest(Message):

    id:int = None
    person:Person = None

@dataclass
class UpdatePersonResponse(Message):
    pass