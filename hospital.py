from concurrent.futures import ThreadPoolExecutor
from decoradores import registrar_historial
from personas import Paciente, Doctor


class Hospital:
    def __init__(self):
        self.pacientes = []
        self.doctores = []

    @registrar_historial  # Registra la admisión de un paciente
    def admitir_paciente(self, paciente: Paciente):
        """Admite un nuevo paciente en el hospital y lo agrega a la lista de pacientes."""
        self.pacientes.append(paciente)

    @registrar_historial  # Esto registra la asignación de un doctor a un paciente
    def asignar_doctor(self, doctor: Doctor, paciente: Paciente):
        """Asigna un doctor a un paciente."""
        paciente.doctor_asignado = doctor
        if doctor not in self.doctores:
            self.doctores.append(doctor)
        doctor.asignar_paciente(paciente)  # Agrega el paciente a la lista del doctor

    def procesar_admisiones(self, lista_pacientes):
        """Procesa las admisiones de una lista de pacientes en paralelo."""
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(self.admitir_paciente, lista_pacientes)
