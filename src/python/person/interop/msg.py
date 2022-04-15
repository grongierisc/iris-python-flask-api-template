from dataclasses import dataclass
from grongier.pex import Message
from .obj import Person

@dataclass
class CreatePersonRequest(Message):

    Person:Person = None

@dataclass
class CreatePersonResponse(Message):

    Status:int=None

@dataclass
class GetAllPersonResponse(Message):

    Persons:[Person] = None

@dataclass
class GetAllPersonResquest(Message):

    currPage:int=None
    pageSize:int=None

@dataclass
class GetPersonResponse(Message):

    Person:Person = None

@dataclass
class GetPersonRequest(Message):

    Id:int = None