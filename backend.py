import sqlite3
import os

rootDirectory = os.path.dirname(os.path.abspath(__file__))

def set_connection():
    conn = sqlite3.connect(os.path.join(rootDirectory, 'myInfoDb.db'))
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS usersInfo ( id INTEGER PRIMARY KEY, name TEXT, age INTEGER, profession TEXT, userID TEXT )")
    conn.commit()
    conn.close()

def insert(name, age, pro, id):
    conn = sqlite3.connect(os.path.join(rootDirectory, 'myInfoDb.db'))
    cur = conn.cursor()
    cur.execute("INSERT INTO usersInfo VALUES(NULL,?,?,?,?)", (name, age, pro, id))
    conn.commit()
    conn.close()

def viewAll():
    conn = sqlite3.connect(os.path.join(rootDirectory, 'myInfoDb.db'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM usersInfo")
    rows = cur.fetchall()
    conn.close()
    return rows


def searchParticular(name="", age="", pro="", id=""):
    conn = sqlite3.connect(os.path.join(rootDirectory, 'myInfoDb.db'))
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM usersInfo WHERE name=? OR age=? OR profession=? OR userID=?", (name, age, pro, id))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect(os.path.join(rootDirectory, 'myInfoDb.db'))
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM usersInfo WHERE id=?", (id,))
    conn.commit()    
    conn.close()

def update(id,name, age, pro, Uid):
    conn = sqlite3.connect(os.path.join(rootDirectory, 'myInfoDb.db'))
    cur = conn.cursor()
    cur.execute(
        "UPDATE usersInfo SET name=?,age=?,profession=?,userID=? WHERE id=?", (name, age, pro, Uid, id))
    conn.commit()
    conn.close()


set_connection()

