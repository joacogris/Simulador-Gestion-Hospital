from personas import Paciente, Doctor
from hospital import Hospital


def main():
    # Crear una instancia de Hospital
    hospital = Hospital()

    # Crea un doctor
    doctor = Doctor("Dr. Alustiza", 45, "Cardiología")

    # Crea  pacientes
    paciente1 = Paciente("Enrique Alderete", 30, "Fractura")
    paciente2 = Paciente("Maria Lopez", 25, "Asma")

    # Admite los pacientes en el hospital
    hospital.admitir_paciente(paciente1)
    hospital.admitir_paciente(paciente2)

    # Asignar el doctor al primer paciente
    hospital.asignar_doctor(doctor, paciente1)

    # Mostraar la información del doctor y los paciente
    print(doctor.obtener_info())
    print("Pacientes de", doctor._nombre, ":", doctor.obtener_pacientes())
    print(paciente1.obtener_info())
    print(paciente2.obtener_info())

    # Se deberian procesar admisiones adicionales en paralelo (por si hubiera una cola más larga de pacientes)
    hospital.procesar_admisiones(
        [paciente1, paciente2]
    )  # Admite los pacientes simultaneamente


if __name__ == "__main__":
    main()
