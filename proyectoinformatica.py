estudiantes = {
    "Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},
    "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},
    "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
}
def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    materias = input("Ingrese las materias aprobadas (separadas por comas): ").split(", ")
    estudiantes[nombre] = {"edad": edad, "materias": materias}
    print(f"Estudiante {nombre} agregado correctamente.\n")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    for nombre, datos in estudiantes.items():
        print(f"Nombre: {nombre}, Edad: {datos['edad']}, Materias: {', '.join(datos['materias'])}")
    print()

def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado correctamente.\n")
    else:
        print("El estudiante no se encuentra en la lista.\n")

def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        datos = estudiantes[nombre]
        print(f"Nombre: {nombre}, Edad: {datos['edad']}, Materias: {', '.join(datos['materias'])}\n")
    else:
        print("El estudiante no está en la lista.\n")

def buscar_por_palabra_clave():
    palabra = input("Ingrese la palabra clave a buscar en los nombres: ").lower()
    encontrados = [nombre for nombre in estudiantes if palabra in nombre.lower()]
    if encontrados:
        print("Estudiantes encontrados:")
        for nombre in encontrados:
            print(f"- {nombre}")
        print()
    else:
        print("No se encontraron estudiantes con esa palabra clave.\n")

def menu():
    while True:
        print("Menú:")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Eliminar estudiante")
        print("4. Buscar estudiante por nombre")
        print("5. Buscar por palabra clave en nombres")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                agregar_estudiante()
            case "2":
                mostrar_estudiantes()
            case "3":
                eliminar_estudiante()
            case "4":
                buscar_estudiante()
            case "5":
                buscar_por_palabra_clave()
            case "6":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, intente nuevamente.\n")

menu()