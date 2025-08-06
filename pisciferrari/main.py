from tkinter import *
from tkinter import messagebox
import sqlite3

ventana = Tk()
ventana.title("Calculadora con BD")
ventana.geometry("400x400")

numero1 = StringVar()
numero2 = StringVar()
numero3 = StringVar()
resultado = StringVar()
numero1.set("")
numero2.set("")
numero3.set("")

conn = sqlite3.connect("calculadora.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS resultados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resultado REAL
    )
""")
conn.commit()
conn.close()

def registrar_resultado(res):
    conn = sqlite3.connect("calculadora.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO resultados (resultado) VALUES (?)", (res,))
    conn.commit()
    conn.close()

def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operación es: {resultado.get()}")

def listar_resultados():
    conn = sqlite3.connect("calculadora.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM resultados")
    registros = cursor.fetchall()
    conn.close()
    texto = "\n".join([f"ID: {r[0]} - Resultado: {r[1]}" for r in registros])
    if texto:
        messagebox.showinfo("Historial de resultados", texto)
    else:
        messagebox.showinfo("Historial vacío", "No hay resultados registrados.")

def operar(operacion):
    try:
        n1 = float(numero1.get())
        n2 = float(numero2.get())
        n3 = float(numero3.get())
        if operacion == "sumar":
            res = n1 + n2 + n3
        elif operacion == "restar":
            res = n1 - n2 - n3
        elif operacion == "multiplicar":
            res = n1 * n2 * n3
        elif operacion == "dividir":
            res = n1 / n2 / n3
        resultado.set(res)
        registrar_resultado(res)
        mostrarResultado()
    except:
        messagebox.showerror("Error", "Introduce bien los datos")
        numero1.set("")
        numero2.set("")
        numero3.set("")

marco = Frame(ventana, width=350, height=250)
marco.config(padx=15, pady=15, bd=5, relief=SOLID)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número").pack()
Entry(marco, textvariable=numero1, justify="center").pack()
Label(marco, text="Segundo número").pack()
Entry(marco, textvariable=numero2, justify="center").pack()
Label(marco, text="Tercer número").pack()
Entry(marco, textvariable=numero3, justify="center").pack()

Button(marco, text="Sumar", command=lambda: operar("sumar")).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=lambda: operar("restar")).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=lambda: operar("multiplicar")).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=lambda: operar("dividir")).pack(side="left", fill=X, expand=YES)

Button(ventana, text="Ver historial de resultados", command=listar_resultados).pack(pady=10)

ventana.mainloop()
