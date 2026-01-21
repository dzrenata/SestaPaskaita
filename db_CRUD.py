import mysql.connector

# pip install mysql-connector-python


DB_CONFIG = {
    'host':'localhost',
    'port': 3306,
    'user':'root',
    'password':'root',
    'database':'pets'
}

headers = ['id', 'name', 'species', 'birth_year']
def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

def load_pets():
    conn = get_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("select * from pets")
    pets = cur.fetchall()
    cur.close()
    conn.close()
    return pets

def print_info():
    print("------------------------------------------------------------")
    print("1. Atvaizduoti augintinius")
    print("2. Pridėti augintinį")
    print("3. Redaguoti augintinį")
    print("4. Šalinti augintinį")
    print("5. Išeiti iš programos")
    print("---------------------- Pasirinkite: -------------------------")

def print_pets():
    pets = load_pets()
    for pet in pets:
        print(f"{pet['id']}. {pet['name']} – {pet['species']}, gimimo metai: {pet['birth_year']}")

def create_pet():
    print("Augintinio pridėjimas")
    print("Įveskite vardą:")
    name = input()
    print("Įveskite rūšį:")
    species = input()
    print("Įveskite gimimo metus:")
    birth_year = int(input())

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO pets(name, species, birth_year) VALUES(%s,%s,%s)",(name, species, birth_year))
    conn.commit()
    cur.close()
    conn.close()

def edit_pet():
    print("Augintinio redagavimas")
    print("Įveskite augintinio ID:")
    edit_id = input()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from pets where id = %s", (edit_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        print(f"Redaguojamas: {row[0]}. {row[1]} – {row[2]}, gimimo metai: {row[3]}")
        print("Naujas vardas:")
        name = input()
        print("Nauja rūšis:")
        species = input()
        print("Nauji gimimo metai:")
        birth_year = int(input())
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "UPDATE pets SET name = %s,species = %s,birth_year =%s WHERE id =%s;",
            (name, species, birth_year, edit_id)
        )
        conn.commit()
        cur.close()
        conn.close()
    else:
        print("Įrašo su tokiu id nėra.")

def remove_pet():
    print("Augintinio šalinimas")
    print("Įveskite augintinio ID:")
    del_id = input()

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pets WHERE id = %s", (del_id,))
    row = cur.fetchone()

    if row:
        print(f"Šalinamas: {row[0]}. {row[1]} – {row[2]}, gimimo metai: {row[3]}")
        cur.execute("DELETE FROM pets WHERE id = %s", (del_id,))
        conn.commit()
    else:
        print("Įrašo su tokių id nėra.")

    cur.close()
    conn.close()
