import unittest

from src.core.hospital import Hospital
from system.ward import Ward

class HospitalTest(unittest.TestCase):

    def test_team_initial_length(self) -> None:
        hospital = Hospital()
        self.assertEqual(len(hospital.teams), 0)

    def test_ward_initial_length(self) -> None:
        hospital = Hospital()
        self.assertEqual(len(hospital.wards), 0)

    def test_add_ward(self) -> None:
        hospital = Hospital()
        hospital.add_ward(0)
        self.assertTrue(isinstance(hospital.wards[-1], Ward))

    def test_add_ward_length(self) -> None:
        hospital = Hospital()
        hospital.add_ward(0)
        self.assertEqual(len(hospital.wards), 1)