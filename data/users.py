import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    gender: str
    mobile: str
    email: str | None
    date_of_birth: str | None
    subjects: str | None
    hobbies: str | None
    image: str | None
    current_address: str | None
    state: str | None
    city: str | None
