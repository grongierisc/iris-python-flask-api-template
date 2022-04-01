from dataclasses import dataclass
import grongier.pex
from interop.obj.ClassPerson import Person

@dataclass
class CreatePersonRequest(grongier.pex.Message):

    Person:Person = None

@dataclass
class CreatePersonResponse(grongier.pex.Message):
    Status:int=None