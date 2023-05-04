from __future__ import annotations

#from person.doctor import Doctor
#from person.patient import Patient

class Appoiment:

    def __init__(self, doctor: "Doctor", patient: "Patient") -> None:
        self.__doctor = doctor
        self.__patient = patient

        self.__doctor.add_appoiment(self)
        self.__patient.add_appoiment(self)

    @property
    def doctor(self) -> "Doctor":
        return self.__doctor