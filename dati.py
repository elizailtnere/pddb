import sqlite3

conn = sqlite3.connect("dati.db", check_same_thread=False)

def lietotaja_tabulas_izveide():
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS lietotaji (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        lietotajvards TEXT NOT NULL UNIQUE
        FROM lietotaji ORDER BY vards ASC
    );
    ''')

conn.commit()

def zinojumu_delis_izveide():
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS ziņas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lietotajvards TEXT NOT NULL,
        ziņa TEXT NOT NULL,
        FOREIGN KEY (lietotajvards) REFERENCES lietotaji (lietotajvards)
    );
    ''')
    
conn.commit()

def pievienot_lietotaju(vards, uzvards, lietotajvards):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO lietotaji (vards, uzvards, lietotajvards)
        VALUES (?, ?, ?)
    ''', (vards, uzvards, lietotajvards))

conn.commit()
    

def pievienot_zinojumu(lietotajs_id, zina):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO zinas (lietotajs_id, zina)
        VALUES (?, ?)
    ''', (lietotajs_id, zina))
    
conn.commit()



def iegut_lietotajus():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM lietotaji')
    lietotaji = cursor.fetchall()
    conn.close()
    return lietotaji


def iegut_zinas():
    cursor = conn.cursor()
    cursor.execute('''
        SELECT lietotaji.vards, lietotaji.uzvards, zinas.zinas
        FROM zinas
        JOIN lietotaji ON lietotaji.id = zinas.lietotajs_id
    ''')
    zina = cursor.fetchall()
    conn.close()
    return zina

def iegut_statistiku():
    cursor = conn.cursor()
    cursor.execute('''
        SELECT lietotaji.vards, lietotaji.uzvards, COUNT(zinas.id) AS zina_skaits
        FROM lietotaji
        LEFT JOIN zinas ON lietotaji.id = zinas.lietotajs_id
        GROUP BY lietotaji.id
    ''')
    
    statistika = cursor.fetchall()
    conn.close()
    return statistika
