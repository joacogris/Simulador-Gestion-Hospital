from abc import ABC, abstractmethod
from decoradores import (
    registrar_historial,
)


class PersonaGeneral(ABC):
    """Interfaz abstracta para la clase Persona, que define el método obtener_info."""

    @abstractmethod
    def obtener_info(self):
        pass


class Persona(PersonaGeneral):
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad

    def obtener_info(self):
        return f"{self._nombre}, {self._edad} años"


class Paciente(Persona):
    def __init__(self, nombre: str, edad: int, condicion: str):
        super().__init__(nombre, edad)
        self._condicion = condicion
        self.doctor_asignado = None

    @registrar_historial  # Registra el historial cuando se actualiza la condición
    def actualizar_condicion(self, nueva_condicion: str):
        """Actualiza la condición médica del paciente."""
        self._condicion = nueva_condicion

    def obtener_info(self):
        doctor_info = (
            self.doctor_asignado.obtener_info()
            if self.doctor_asignado
            else "No Asignado"
        )
        return f"Paciente: {super().obtener_info()}, Condición: {self._condicion}, Doctor: {doctor_info}"


class Doctor(Persona):
    def __init__(self, nombre: str, edad: int, especialidad: str):
        super().__init__(nombre, edad)
        self._especialidad = especialidad
        self.pacientes = []

    @registrar_historial
    def asignar_paciente(self, paciente: Paciente):
        """Asigna un paciente al doctor y establece el doctor en el paciente."""
        self.pacientes.append(paciente)
        paciente.doctor_asignado = self

    def obtener_info(self):
        return f"Doctor: {self._nombre}, Especialidad: {self._especialidad}"

    def obtener_pacientes(self):
        return [paciente.obtener_info() for paciente in self.pacientes]
