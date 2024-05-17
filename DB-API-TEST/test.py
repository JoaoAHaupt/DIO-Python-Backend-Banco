"""
Teste de conexão com banco de dados SQLITE usando DB API
"""

import sqlite3

con = sqlite3.connect("database.db")

cur = con.cursor()


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(50), email VARCAHR(40), cpf VARCHAR(11));")


def inserir_cliente(conexao, cursor, nome, email, cpf):
    data = (nome, email, cpf)
    cursor.execute("INSERT INTO clientes (nome, email, cpf) VALUES (?, ?, ?), data")
    conexao.commit()

def inserir_varios_clientes(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email, cpf) VALUES (?, ?, ?)", dados)
    conexao.commit()


def atualizar_cliente(conexao, cursor, nome, email, cpf, id):
    data = (nome, email, cpf, id)
    cursor.execute("UPDATE clientes SET nome=?, email=?, cpf=? WHERE id=?", data)
    conexao.commit()

def remover_cliente(conexao, cursor,id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
    conexao.commit()

def procurar_cliente(cursor,id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes")
    return cursor.fetchall()

print(procurar_cliente(cur, 2))

print(listar_clientes(cur))




