from grongier.pex import Message
from dataclasses import dataclass

@dataclass
class Priority(Message):
    value: int