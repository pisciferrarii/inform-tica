import sqlite3

# Crear o conectar a la base de datos
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY,
    titulo TEXT,
    autor TEXT,
    anio INTEGER,
    genero TEXT
)
''')
conn.commit()

# Funciones
def agregar_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = int(input("Año: "))
    genero = input("Género: ")
    cursor.execute("INSERT INTO libros (titulo, autor, anio, genero) VALUES (?, ?, ?, ?)",
                   (titulo, autor, anio, genero))
    conn.commit()
    print("Libro agregado con éxito.\n")

def modificar_libro():
    id_libro = int(input("ID del libro a modificar: "))
    nuevo_titulo = input("Nuevo título: ")
    nuevo_autor = input("Nuevo autor: ")
    nuevo_anio = int(input("Nuevo año: "))
    nuevo_genero = input("Nuevo género: ")
    cursor.execute('''
        UPDATE libros
        SET titulo = ?, autor = ?, anio = ?, genero = ?
        WHERE id = ?
    ''', (nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_genero, id_libro))
    conn.commit()
    print("Libro modificado con éxito.\n")

def mostrar_libros():
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    if libros:
        for libro in libros:
            print(libro)
    else:
        print("No hay libros en la base de datos.")
    print()

def eliminar_libro():
    id_libro = int(input("ID del libro a eliminar: "))
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conn.commit()
    print("Libro eliminado con éxito.\n")

def buscar_libro():
    titulo = input("Ingrese el título del libro a buscar: ")
    cursor.execute("SELECT * FROM libros WHERE titulo LIKE ?", ('%' + titulo + '%',))
    resultados = cursor.fetchall()
    if resultados:
        for libro in resultados:
            print(libro)
    else:
        print("No se encontraron libros con ese título.")
    print()

# Menú
def menu():
    while True:
        print("\n--- Menú de la Biblioteca ---")
        print("1. Agregar libro")
        print("2. Modificar libro")
        print("3. Mostrar libros")
        print("4. Eliminar libro")
        print("5. Buscar libro")
        print("6. Salir")

        opcion = input("Seleccioná una opción: ")

        match opcion:
            case "1":
                agregar_libro()
            case "2":
                modificar_libro()
            case "3":
                mostrar_libros()
            case "4":
                eliminar_libro()
            case "5":
                buscar_libro()
            case "6":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida, intentá de nuevo.")

# Ejecutar el menú
menu()

# Cerrar conexión
conn.close()
