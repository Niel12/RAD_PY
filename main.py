import sqlite3 #importação biblioteca sqlite
banco = sqlite3.connect('database.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE cliente(nome text, idade int, sex text)")
#cursor.execute("INSERT INTO cliente VALUES('Cyntia', 40, 'F'), ('Pedro', 10, 'M')")
#cursor.execute("DELETE FROM cliente WHERE nome='Pedro'")
banco.commit()
cursor.close()
banco.close()