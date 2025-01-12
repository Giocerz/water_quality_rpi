from typing import Optional

class LoteModel:
    def __init__(
        self,
        name: str,
        creation_date: str,
        creation_hour: str,
        last_add_date: str,
        last_add_hour: str,
        id: Optional[int] = None,
        description: Optional[str] = None
    ):

        self.id: Optional[int] = id
        self.name: str = name
        self.creation_date: str = creation_date
        self.creation_hour: str = creation_hour
        self.last_add_date: str = last_add_date
        self.last_add_hour: str = last_add_hour
        self.description: Optional[str] = description

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'creation_date': self.creation_date,
            'creation_hour': self.creation_hour,
            'last_add_date': self.last_add_date,
            'last_add_hour': self.last_add_hour,
            'description': self.description
        }