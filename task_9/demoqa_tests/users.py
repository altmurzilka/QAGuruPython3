import dataclasses

import dataclasses
from enum import Enum
from typing import List


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject(Enum):
    english = 'English'
    maths = 'Maths'
    physics = 'Physics'
    chemistry = 'Chemistry'
    computer_science = 'Computer Science'
    economics = 'Economics'
    arts = 'Arts'
    biology = 'Biology'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: List[Gender]
    mobile: str
    day: str
    month: str
    year: str
    subjects: List[Subject]
    hobbies: List[Hobby]
    picture: str
    address: str
    state: str
    city: str
