import unittest
from hospital import Hospital
from personas import Paciente, Doctor


class TestHospital(unittest.TestCase):
    def test_admision_paciente(self):
        hospital = Hospital()
        paciente = Paciente("Juan Perez", 30, "Fractura")
        hospital.admitir_paciente(paciente)
        self.assertIn(paciente, hospital.pacientes)

    def test_asignacion_doctor_a_paciente(self):
        hospital = Hospital()
        doctor = Doctor("Dr. Smith", 45, "Cardiología")
        paciente = Paciente("Juan Perez", 30, "Fractura")

        hospital.admitir_paciente(paciente)
        hospital.asignar_doctor_a_paciente(doctor, paciente)

        # Esto verifica que el paciente tiene el doctor asignado
        self.assertEqual(paciente.doctor_asignado, doctor)
        # Aqui verifica que el doctor tiene el paciente asignado
        self.assertIn(paciente, doctor.pacientes)
        # Se verifica que el doctor se ha agregado a la lista de doctores del hospital
        self.assertIn(doctor, hospital.doctores)


if __name__ == "__main__":
    unittest.main()
