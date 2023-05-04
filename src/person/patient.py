from __future__ import annotations
from typing import List

#from person.doctor import Doctor
from system.appoiment import Appoiment
#from system.team import Team
#from system.ward import Ward

class Patient:

    def __init__(self, id: int, team: "Team", ward: "Ward") -> None:
        self.__id = id
        self.__team = team
        self.__ward = ward
        self.__appoiments: List["Appoiment"] = []
        self.__doctors: List["Doctor"] = []

        self.__team.add_patient(self)
        self.__ward.add_patient(self)

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def team(self) -> "Team":
        return self.__team
    
    @property
    def ward(self) -> "Ward":
        return self.__ward
    
    def add_doctor(self, doctor: "Doctor") -> bool:
        self.__doctors.append(doctor)
        return True
    
    def add_appoiment(self, appoiment: "Appoiment") -> bool:
        self.__appoiments.append(appoiment)
        return True
    
    def get_doctors_id(self) -> List[int]:
        return [appoiment.doctor.id for appoiment in self.__appoiments]

    def number_of_appoiments(self) -> int:
        return len(self.__appoiments)

    def number_of_doctors(self) -> int:
        return len(self.__doctors)