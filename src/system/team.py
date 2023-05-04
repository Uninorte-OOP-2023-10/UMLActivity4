from __future__ import annotations
from typing import List, Optional

#from person.doctor import ConsultantDoctor, Doctor
from person.patient import Patient

class Team:

    def __init__(self, id: int) -> None:
        self.__id = id
        self.__team_leader: Optional["ConsultantDoctor"] = None
        self.__doctors: List["Doctor"] = []
        self.__patients: List["Patient"] = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def team_leader(self) -> "ConsultantDoctor":
        return self.__team_leader
    
    @team_leader.setter
    def team_leader(self, leader: "ConsultantDoctor") -> bool:
        self.__team_leader = leader
        return True
    
    @property
    def doctors(self) -> List["Doctor"]:
        return self.__doctors
    
    @property
    def patients(self) -> List["Patient"]:
        return self.__patients

    def add_doctor(self, doctor: "Doctor") -> bool:
        self.__doctors.append(doctor)
        return True
    
    def add_patient(self, patient: "Patient") -> bool:
        self.__patients.append(patient)

    def number_of_patients(self) -> int:
        return len(self.__patients)