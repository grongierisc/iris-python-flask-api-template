from dataclasses import dataclass
import grongier.pex
from interop.obj.ClassPerson import Person

@dataclass
class GetPersonResponse(grongier.pex.Message):

    Person:Person = None

@dataclass
class GetPersonRequest(grongier.pex.Message):

    Id:int = None