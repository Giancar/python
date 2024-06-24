import sqlite3
from Usuario import Usuario

class DatabaseManager:
    def __init__(self, db_name = 'usuarios.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_user(self, usuario):
        self.cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (usuario.nome, usuario.email))
        self.conn.commit()

    def get_users(self):
        self.cursor.execute('SELECT * FROM usuarios')
        return [Usuario(nome=row[1], email=row[2], user_id=row[0]) for row in self.cursor.fetchall()]

    def update_user(self, usuario):
        self.cursor.execute('UPDATE usuarios SET nome = ?, email = ? WHERE id = ?', (usuario.nome, usuario.email, usuario.id))
        self.conn.commit()

    def delete_user(self, usuario):
        self.cursor.execute('DELETE FROM usuarios WHERE id = ?', (usuario.id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()