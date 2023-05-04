from __future__ import annotations

from core.hospital import Hospital

def main() -> None:
    hospital = Hospital()

    hospital.add_team(0, 0 + 10) # 0 is the Team id. The Team id plus 10 is the ConsultantDoctor id.
    hospital.add_junior_doctor(hospital.get_team(0), 0 + 1) # Receives the Team. The Team id plus value is the JuniorDoctor id.
    hospital.add_junior_doctor(hospital.get_team(0), 0 + 2)
    hospital.add_junior_doctor(hospital.get_team(0), 0 + 3)
    hospital.add_junior_doctor(hospital.get_team(0), 0 + 4)

    hospital.add_team(100, 100 + 10)
    hospital.add_junior_doctor(hospital.get_team(100), 100 + 1)
    hospital.add_junior_doctor(hospital.get_team(100), 100 + 2)
    hospital.add_junior_doctor(hospital.get_team(100), 100 + 3)
    hospital.add_junior_doctor(hospital.get_team(100), 100 + 4)

    hospital.add_team(200, 200 + 10)
    hospital.add_junior_doctor(hospital.get_team(200), 200 + 1)
    hospital.add_junior_doctor(hospital.get_team(200), 200 + 2)
    hospital.add_junior_doctor(hospital.get_team(200), 200 + 3)
    hospital.add_junior_doctor(hospital.get_team(200), 200 + 4)

    hospital.add_ward(10)

    hospital.add_patient(hospital.get_ward(10), hospital.get_team(0), 0 + 10) # Receives the Ward, the Team and the Patient id.
    hospital.assign_patient_doctor(hospital.get_patient(0 + 10), 1) # Receives the Patient and the Doctor id is the Patient Team id plus the second function parameter (int).
    hospital.assign_patient_doctor(hospital.get_patient(0 + 10), 2)
    hospital.assign_appoiment(hospital.get_patient(0 + 10), 2) # The parameter values are the same as assign_patient_doctor.
    hospital.assign_appoiment(hospital.get_patient(0 + 10), 2)
    hospital.assign_appoiment(hospital.get_patient(0 + 10), 2)

    hospital.add_patient(hospital.get_ward(10), hospital.get_team(100), 1 + 10)
    hospital.assign_patient_doctor(hospital.get_patient(1 + 10), 1)

    hospital.add_patient(hospital.get_ward(10), hospital.get_team(100), 2 + 10)
    hospital.assign_patient_doctor(hospital.get_patient(2 + 10), 1)
    hospital.assign_appoiment(hospital.get_patient(2 + 10), 1)
    hospital.assign_appoiment(hospital.get_patient(2 + 10), 1)
    hospital.assign_appoiment(hospital.get_patient(2 + 10), 1)
    hospital.assign_appoiment(hospital.get_patient(2 + 10), 1)
    hospital.assign_patient_doctor(hospital.get_patient(2 + 10), 2)
    hospital.assign_patient_doctor(hospital.get_patient(2 + 10), 3)
    hospital.assign_appoiment(hospital.get_patient(2 + 10), 3)
    hospital.assign_appoiment(hospital.get_patient(2 + 10), 3)

    hospital.add_patient(hospital.get_ward(10),hospital.get_team(0), 3 + 10)
    hospital.assign_patient_doctor(hospital.get_patient(3 + 10), 1)
    hospital.assign_appoiment(hospital.get_patient(3 + 10), 1)

    hospital.add_ward(50)

    hospital.add_patient(hospital.get_ward(50), hospital.get_team(0), 0 + 50)
    hospital.assign_patient_doctor(hospital.get_patient(0 + 50), 1)
    hospital.assign_patient_doctor(hospital.get_patient(0 + 50), 2)
    hospital.assign_appoiment(hospital.get_patient(0 + 50), 1)
    hospital.assign_appoiment(hospital.get_patient(0 + 50), 1)
    hospital.assign_appoiment(hospital.get_patient(0 + 50), 1)
    hospital.assign_patient_doctor(hospital.get_patient(0 + 50), 3)
    hospital.assign_patient_doctor(hospital.get_patient(0 + 50), 4)

    hospital.add_patient(hospital.get_ward(50), hospital.get_team(100), 1 + 50)
    hospital.assign_patient_doctor(hospital.get_patient(1 + 50), 1)

    hospital.add_patient(hospital.get_ward(50), hospital.get_team(200), 2 + 50)
    hospital.assign_patient_doctor(hospital.get_patient(2 + 50), 1)
    hospital.assign_patient_doctor(hospital.get_patient(2 + 50), 2)

    hospital.add_patient(hospital.get_ward(50), hospital.get_team(0), 3 + 50)
    hospital.assign_patient_doctor(hospital.get_patient(3 + 50), 3)
    hospital.assign_appoiment(hospital.get_patient(3 + 50), 3)
    hospital.assign_appoiment(hospital.get_patient(3 + 50), 3)
    hospital.assign_appoiment(hospital.get_patient(3 + 50), 3)
    hospital.assign_appoiment(hospital.get_patient(3 + 50), 3)
    hospital.assign_appoiment(hospital.get_patient(3 + 50), 3)

    print('Number of doctors per patient:')
    hospital.number_doctors_patient()

    print('\nNumber of patients per team:')
    hospital.number_patients_team()

    print('\nList of appointments in the system:')
    hospital.relation_appoiments()


if __name__ == '__main__':
    main()


""" RESULTS
Number of doctors per patient:
Patient 10 has 2 doctors
Patient 11 has 1 doctors
Patient 12 has 3 doctors
Patient 13 has 1 doctors
Patient 50 has 4 doctors
Patient 51 has 1 doctors
Patient 52 has 2 doctors
Patient 53 has 1 doctors

Number of patients per team:
Team 0 has 4 patients
Team 100 has 3 patients
Team 200 has 1 patients

List of appointments in the system:
Patient 10 has 3 appoiments
Patient 10 has an appoiment with the doctor 2
Patient 10 has an appoiment with the doctor 2
Patient 10 has an appoiment with the doctor 2
Patient 11 has 0 appoiments
Patient 12 has 6 appoiments
Patient 12 has an appoiment with the doctor 101
Patient 12 has an appoiment with the doctor 101
Patient 12 has an appoiment with the doctor 101
Patient 12 has an appoiment with the doctor 101
Patient 12 has an appoiment with the doctor 103
Patient 12 has an appoiment with the doctor 103
Patient 13 has 1 appoiments
Patient 13 has an appoiment with the doctor 1
Patient 50 has 3 appoiments
Patient 50 has an appoiment with the doctor 1
Patient 50 has an appoiment with the doctor 1
Patient 50 has an appoiment with the doctor 1
Patient 51 has 0 appoiments
Patient 52 has 0 appoiments
Patient 53 has 5 appoiments
Patient 53 has an appoiment with the doctor 3
Patient 53 has an appoiment with the doctor 3
Patient 53 has an appoiment with the doctor 3
Patient 53 has an appoiment with the doctor 3
Patient 53 has an appoiment with the doctor 3
"""