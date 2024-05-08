tareas = []

while True:
    print("\n~~~ Gestor de Tareas ~~~")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Salir")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == '1':
        if not tareas:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
    elif opcion == '2':
        nueva_tarea = input("Ingrese la descripción de la tarea: ")
        tareas.append(nueva_tarea)
        print("Tarea agregada correctamente.")
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")