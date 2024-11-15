def registrar_historial(funcion):
    def guardar_historial(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        with open("historial.txt", "a") as file:
            file.write(f"{funcion.__name__} llamado con {args}, {kwargs}\n")
        return resultado

    return guardar_historial
