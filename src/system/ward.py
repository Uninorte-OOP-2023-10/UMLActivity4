from __future__ import annotations
from typing import List

from person.patient import Patient

class Ward:

    def __init__(self, id: int) -> None:
        self.__id = id
        self.__patients: List["Patient"] = []

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def patients(self) -> List["Patient"]:
        return self.__patients
    
    def add_patient(self, patient: "Patient") -> bool:
        self.__patients.append(patient)
        return True