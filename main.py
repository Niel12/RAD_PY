import sqlite3
from modelo import Pessoa, Marca, Veiculo

banco = sqlite3.connect('database.db')
banco.execute("PRAGMA foreign_keys=on")
cursor = banco.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa(
                cpf INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                nascimento DATE NOT NULL,
                oculos BOOLEAN NOT NULL
                );''') 
cursor.execute('''CREATE TABLE IF NOT EXISTS Marca(
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                sigla CHARACTER(2) NOT NULL,
                PRIMARY KEY(id)           
);''') 
cursor.execute('''CREATE TABLE IF NOT EXISTS Veiculo(
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY(placa),
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES Marca(id));''')

#cursor.execute('''ALTER TABLE Veiculo ADD motor REAL;''')
#Adcionando Pessoa
pessoa = Pessoa(32112312142, 'JOSEUF', '3000-10-21', False)
comando = ('''INSERT INTO Pessoa (cpf, nome, nascimento,oculos) VALUES(:cpf, :nome, :nascimento, :usa_oculos)''')
cursor.execute(comando, vars(pessoa))

#adcionar Marca
comando = '''INSERT INTO Marca(nome, sigla) VALUES(:nome, :sigla)'''
marcaA = Marca("Marca A", "MA")
cursor.execute(comando, vars(marcaA))
marcaA.id = cursor.lastrowid
marcaB = Marca("Marca B", "MB")
cursor.execute(comando, vars(marcaB))
marcaB.id = cursor.lastrowid

#Adcionar Veiculo
comando = ''' INSERT INTO Veiculo(placa, ano, cor, motor, propietario, marca) VALUES(:placa, :ano, :cor, :motor, :propietario, :marca)'''
Veiculo1 = Veiculo( "A15S4511", "2020", "ROSA", 1.6, 12312312312, marcaA.id )
cursor.execute(comando, vars(Veiculo1))

banco.commit()
banco.close()