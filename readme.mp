# Simulador de Gestión de Hospital

Este proyecto es un **Simulador de Gestión de turnos de Hospital** desarrollado en Python. 
Permite gestionar pacientes, doctores y tratamientos en un entorno simulado, 
aplicando varios conceptos avanzados de programación como programación orientada a objetos, 
concurrencia y uso de decoradores.

## Requisitos Previos:

Asegúrarse de tener instalada una versión de Python 3.6 o superior. 
Puede verificar tu versión de Python ejecutando el siguiente comando:

```terminal 
python --version
Instalación
Clona el repositorio o descarga el proyecto en tu máquina o pc local.

Crea un entorno virtual (recomiendo) para instalar las dependencias del proyecto.

terminal 

python -m venv env
Activa el entorno virtual (recomiendo):

En Windows:

terminal 

.\env\Scripts\activate

En macOS/Linux:

terminal

source env/bin/activate
Instala las dependencias necesarias. Este proyecto no tiene dependencias externas, 
pero si en el futuro se agregan, puedes instalarlas usando pip install -r requirements.txt si el archivo existe.

Estructura del Proyecto
El proyecto está dividido en los siguientes archivos:

personas.py: Contiene las clases Persona, Paciente, y Doctor.
decoradores.py: Contiene decoradores utilizados para registrar acciones dentro del sistema.
hospital.py: Contiene el decorador registrar_historial, que permite registrar automáticamente 
en un archivo historial.txt las acciones realizadas (como admisiones y asignaciones de doctores).
tests/test_hospital.py: Contiene las pruebas unitarias para verificar la funcionalidad de las clases y métodos.
main.py: Punto de entrada del programa, donde se simulan las operaciones del hospital.
Uso
Ejecuta el archivo principal para iniciar la simulación:

terminal

python main.py
Ejemplo de ejecución: Al ejecutar main.py, el programa creará una instancia de Doctor, 
asignará un Paciente, y mostrará la información de ambos.

Un ejemplo de Código
Aquí hay un ejemplo básico de cómo se configura y usa el programa en main.py:

python

from personas import Paciente, Doctor
from hospital import Hospital


def main():
    # Crear una instancia de Hospital
    hospital = Hospital()

    # Crea un doctor
    doctor = Doctor("Dr. Yocca", 45, "Cardiología")

    # Crea  pacientes
    paciente1 = Paciente("Juan Perez", 30, "Fractura")
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

    # Se deberian procesar admisiones adicionales en paralelo (por si hubiera una lista más larga de pacientes)
    hospital.procesar_admisiones(
        [paciente1, paciente2]
    )  # Admite los pacientes simultaneamente


if __name__ == "__main__":
    main()



Pruebas Unitarias
Este proyecto incluye tambien pruebas unitarias para verificar el correcto 
funcionamiento de cada clase y método. Para ejecutar las pruebas, utiliza el siguiente comando:

terminal

python -m unittest discover -s tests

Las pruebas están ubicadas en el directorio tests, y validan la creación de instancias, 
la asignación de doctores a pacientes y otras funcionalidades clave del proyecto.

Pautas
Este proyecto sigue o intenta seguir las guías de estilo de PEP8. 