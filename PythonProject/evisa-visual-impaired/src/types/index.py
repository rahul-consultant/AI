# This file defines data types and structures used throughout the application.

from typing import Optional, Dict, Any

class UserInput:
    def __init__(self, firstname: Optional[str] = None, lastname: Optional[str] = None,
                 address: Optional[str] = None, gender: Optional[str] = None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.gender = gender

class CollectedData:
    def __init__(self) -> None:
        self.data: Dict[str, Any] = {
            "firstname": None,
            "lastname": None,
            "address": None,
            "gender": None
        }

    def is_complete(self) -> bool:
        return all(value is not None for value in self.data.values())

    def update(self, field: str, value: str) -> None:
        if field in self.data:
            self.data[field] = value