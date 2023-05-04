from __future__ import annotations
from abc import ABC
from typing import List

from person.patient import Patient
from system.appoiment import Appoiment
from system.team import Team

class Doctor(ABC):

    def __init__(self, id: int, team: "Team") -> None:
        self._id = id
        self._team = team
        self._appoiments: List["Appoiment"] = []
        self._patients: List["Patient"] = []

        self._team.add_doctor(self)

    @property
    def id(self) -> int:
        return self._id
    
    def add_patient(self, patient: "Patient") -> bool:
        self._patients.append(patient)
        return True
    
    def add_appoiment(self, appoiment: "Appoiment") -> bool:
        self._appoiments.append(appoiment)
        return True


class ConsultantDoctor(Doctor):

    def __init__(self, id: int, team: "Team") -> None:
        super().__init__(id, team)
        self.__leader_of = team
        self.__leader_of.team_leader = self


class JuniorDoctor(Doctor):

    def __init__(self, id: int, team: "Team") -> None:
        super().__init__(id, team)