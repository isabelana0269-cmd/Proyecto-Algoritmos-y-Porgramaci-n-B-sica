tareas = []  # Lista para guardar las tareas

def agregar_tarea():
    nombre = input("Escribe el nombre de la tarea: ")
    fecha = input("Escribe la fecha de entrega (ejemplo: 2025-09-30): ")
    tareas.append({"nombre": nombre, "fecha": fecha})
    print("✅ Tarea registrada correctamente.\n")

def mostrar_tareas():
    if len(tareas) == 0:
        print("No tienes tareas registradas.\n")
    else:
        print("Estas son tus tareas pendientes:")
        for t in tareas:
            print("- ", t["nombre"], " | Fecha de entrega:", t["fecha"])
        print("")

def enviar_recordatorio():
    if len(tareas) > 0:
        print("Recordatorio: No olvides tu tarea:", tareas[0]["nombre"], 
              "con fecha:", tareas[0]["fecha"], "\n")
    else:
        print("No hay tareas para recordar.\n")


for i in range(3):
    print("Chatbot de Recordatorios")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Enviar recordatorio")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        enviar_recordatorio()
    elif opcion == "4":
        print("Saliendo del chatbot...\n")
        break
    else:
        print("Opción no válida. Intenta de nuevo.\n")