def mostrar_menu():
    print("\n~~~ Gestor de Tareas ~~~")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. [{tarea['estado']}] {tarea['descripcion']}")

def agregar_tarea(tareas):
    descripcion = input("Ingrese la descripción de la tarea: ")
    tarea = {'descripcion': descripcion, 'estado': 'pendiente'}
    tareas.append(tarea)
    print("Tarea agregada correctamente.")

def marcar_como_completada(tareas):
    ver_tareas(tareas)
    num_tarea = int(input("Ingrese el número de la tarea completada: "))
    if 1 <= num_tarea <= len(tareas):
        tareas[num_tarea - 1]['estado'] = 'completada'
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea inválido.")

def eliminar_tarea(tareas):
    ver_tareas(tareas)
    num_tarea = int(input("Ingrese el número de la tarea a eliminar: "))
    if 1 <= num_tarea <= len(tareas):
        del tareas[num_tarea - 1]
        print("Tarea eliminada correctamente.")
    else:
        print("Número de tarea inválido.")

def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción: ")
        if opcion == '1':
            ver_tareas(tareas)
        elif opcion == '2':
            agregar_tarea(tareas)
        elif opcion == '3':
            marcar_como_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()