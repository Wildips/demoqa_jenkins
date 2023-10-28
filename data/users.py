import dataclasses
from enum import Enum
from typing import List


class Subject(Enum):
    maths = 'Maths'
    chemistry = 'Chemistry'
    english = 'English'
    biology = 'Biology'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    gender: str
    mobile: str
    email: str | None
    date_of_birth: str | None
    subjects: List[Subject] | None
    hobbies: str | None
    image: str | None
    current_address: str | None
    state: str | None
    city: str | None
