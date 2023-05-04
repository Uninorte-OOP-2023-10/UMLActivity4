from __future__ import annotations
from typing import List, Optional

from person.doctor import Doctor, ConsultantDoctor, JuniorDoctor
from person.patient import Patient
from system.appoiment import Appoiment
from system.team import Team
from system.ward import Ward

class Hospital:

    def __init__(self) -> None:
        self.__teams: List["Team"] = []
        self.__wards: List["Ward"] = []

    @property
    def teams(self) -> List["Team"]:
        return self.__teams
    
    @property
    def wards(self) -> List["Ward"]:
        return self.__wards

    def add_junior_doctor(self, team: "Team", doctor_id: int) -> bool:
        junior_doctor = JuniorDoctor(doctor_id, team)
        return True

    def add_patient(self, ward: "Ward", team: "Team", patient_id: int) -> bool:
        patient = Patient(patient_id, team, ward)
        return True

    def add_team(self, team_id: int, consultant_doctor_id: int) -> bool:
        team = Team(team_id)
        consultant_doctor = ConsultantDoctor(consultant_doctor_id, team)
        self.__teams.append(team)
        return True
    
    def add_ward(self, ward_id: int) -> bool:
        self.__wards.append(Ward(ward_id))
        return True
    
    def __get_doctor(self, doctor_id) -> Optional["Doctor"]:
        for team in self.__teams:
            for doctor in team.doctors:
                if doctor.id == doctor_id:
                    return doctor
        return None

    def get_patient(self, patient_id: int) -> Optional["Patient"]:
        for team in self.__teams:
            for patient in team.patients:
                if patient.id == patient_id:
                    return patient
        return None

    def get_team(self, team_id: int) -> Optional["Team"]:
        for team in self.__teams:
            if team.id == team_id:
                return team
        return None
    
    def get_ward(self, ward_id: int) -> Optional["Ward"]:
        for ward in self.__wards:
            if ward.id == ward_id:
                return ward
        return None 
    
    def assign_appoiment(self, patient: "Patient", id_doctor_plus: int) -> bool:
        team_id = patient.team.id
        doctor = self.__get_doctor(team_id + id_doctor_plus)

        appoiment = Appoiment(doctor, patient)
        
        return True

    def assign_patient_doctor(self, patient: "Patient", id_doctor_plus: int) -> bool:
        team_id = patient.team.id
        doctor = self.__get_doctor(team_id + id_doctor_plus)

        patient.add_doctor(doctor)
        doctor.add_patient(patient)
        
        return True
    
    def number_doctors_patient(self) -> None:
        for ward in self.__wards:
            for patient in ward.patients:
                print(f'Patient {patient.id} has {patient.number_of_doctors()} doctors')

    def number_patients_team(self) -> None:
        for team in self.__teams:
            print(f'Team {team.id} has {team.number_of_patients()} patients')

    def relation_appoiments(self) -> None:
        for ward in self.__wards:
            for patient in ward.patients:
                number_of_appoiments = patient.number_of_appoiments()
                print(f'Patient {patient.id} has {number_of_appoiments} appoiments')
                if number_of_appoiments > 0:
                    doctors_id = patient.get_doctors_id()
                    for doctor_id in doctors_id:
                        print(f'Patient {patient.id} has an appoiment with the doctor {doctor_id}')