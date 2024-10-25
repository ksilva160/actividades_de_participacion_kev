


class UIConsola:

    def menu():
    gimnasio = Gimnasio()
    while True:
        print("\n--- Menú del Gimnasio ---")
        print("1. Registrar usuario")
        print("2. Consultar usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            correo = input("Ingrese el correo del usuario: ")
            membresia = input("Ingrese el tipo de membresía: ")
            t_documento = input("Ingrese el tipo de documento: ")
            n_documento = input("Ingrese el número de documento: ")
            usuario = gimnasio.registrar_usuario(nombre, correo, membresia, t_documento, n_documento)
            print("Usuario registrado con éxito.")

            # Registrar detalles adicionales
            fecha_inicio = input("Ingrese la fecha de inicio de la membresía (dd/mm/aaaa): ")
            fecha_final = input("Ingrese la fecha final de la membresía (dd/mm/aaaa): ")
            usuario.estado_membresia(membresia, fecha_inicio, fecha_final)

            altura = input("Ingrese la altura del usuario (ej: 180cm): ")
            peso = input("Ingrese el peso del usuario (ej: 70kg): ")
            medidas_corporales = input("Ingrese las medidas corporales (ej: Cintura 80cm): ")
            fecha_registro = input("Ingrese la fecha de registro de medidas (dd/mm/aaaa): ")
            usuario.medidas_usuarios(altura, peso, medidas_corporales, fecha_registro)

            fecha_asistencia = input("Ingrese la fecha de la asistencia (dd/mm/aaaa): ")
            hora_entrada = input("Ingrese la hora de entrada (ej: 9am): ")
            hora_salida = input("Ingrese la hora de salida (ej: 11am): ")
            duracion_entrenamiento = input("Ingrese la duración del entrenamiento (ej: 2 horas): ")
            usuario.asistencias_usuario(fecha_asistencia, hora_entrada, hora_salida, duracion_entrenamiento)

            print("Datos adicionales registrados con éxito.")

        elif opcion == "2":
            n_documento = input("Ingrese el número de documento del usuario a consultar: ")
            usuario = gimnasio.consultar_usuario(n_documento)
            if usuario:
                print("Usuario encontrado:")
                print(gimnasio.generar_informe(usuario))
            else:
                print("Usuario no encontrado.")

        elif opcion == "3":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# Ejecutar el menú interactivo
menu()
