from dataclasses import dataclass
from grongier.pex import Message
from obj import Person

@dataclass
class CreatePersonRequest(Message):

    person:Person = None

@dataclass
class CreatePersonResponse(Message):

    status:int=None

@dataclass
class GetAllPersonResponse(Message):

    persons:[Person] = None

@dataclass
class GetAllPersonResquest(Message):

    currPage:int=None
    pageSize:int=None

@dataclass
class GetPersonResponse(Message):

    person:Person = None

@dataclass
class GetPersonRequest(Message):

    id:int = None