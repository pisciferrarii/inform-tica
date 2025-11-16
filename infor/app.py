from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    habitaciones = conn.execute('SELECT * FROM habitaciones').fetchall()
    reservas = conn.execute('SELECT * FROM reservas').fetchall()
    conn.close()
    return render_template('index.html', habitaciones=habitaciones, reservas=reservas)

if __name__ == '__main__':
    app.run(debug=True)
