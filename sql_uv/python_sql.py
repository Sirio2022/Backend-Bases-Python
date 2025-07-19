import sqlite3

def inicializar_db():
    with open('clientes.sql', 'r') as f:
        sql_script = f.read()
    conn = sqlite3.connect('bases_curso.sqlite3')
    cursor = conn.cursor()
    # Verifica si la tabla existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clientes';")
    if not cursor.fetchone():
        cursor.executescript(sql_script)
        conn.commit()
    conn.close()

def obtener_clientes():
    conn = sqlite3.connect('bases_curso.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def crear_cliente(nombre, apellido, email, fecha_registro, telefono, role = 'Null'):
    conn = sqlite3.connect('bases_curso.sqlite3')
    cursor = conn.cursor()
    cliente = (nombre, apellido, email, fecha_registro, telefono, role)
    cursor.execute(f"INSERT INTO clientes (nombre, apellido, email, fecha_registro, telefono, role) VALUES {cliente}")
    conn.commit()
    conn.close()

def main():
    inicializar_db()

    # Crear un cliente de ejemplo
    crear_cliente("Juan", "Pérez", "jmapœjmap.com", "2023-10-01", "1234567890", "Admin")
    clientes = obtener_clientes()

    for cliente in clientes:
        print(cliente)

if __name__ == "__main__":
    main()