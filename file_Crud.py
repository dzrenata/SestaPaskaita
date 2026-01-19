import csv

headers = ["id", "name", "species", "birth_year"]

def load_pets():
    with open ("my_pets.csv",mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def save_pets(pets):
    with open ("my_pets.csv",mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(pets)

def print_info():
    print("------------------------------------------------------------")
    print("1. Atvaizduoti augintinius")
    print("2. Pridėti augintinį")
    print("3. Redaguoti augintinį")
    print("4. Šalinti augintinį")
    print("5. Išeiti iš programos")
    print("---------------------- Pasirinkite: -------------------------")

def print_pets(pets):
    for pet in pets:
        print(f"{pet["id"]}. {pet["name"]} – {pet["species"]}, gimimo metai: {pet["birth_year"]}")

def create_pet(pets, id_counter):
    print("Augintinio pridėjimas")
    print("Įveskite vardą:")
    name = input()
    print("Įveskite rūšį:")
    species = input()
    print("Įveskite gimimo metus:")
    birth_year = int(input())
    id_counter = int(pets[-1]["id"]) + 1 if len(pets) > 0 else 1
    pet = {
        "id": id_counter,
        "name": name,
        "species": species,
        "birth_year": birth_year
    }
    pets.append(pet)
    save_pets(pets)
    return id_counter

def edit_pet(pets):
    print("Augintinio redagavimas")
    print("Įveskite augintinio ID:")
    edit_id = input()
    for pet in pets:
        if edit_id == str(pet["id"]):
            print(f"Redaguojamas: {pet["id"]}. {pet["name"]} – {pet["species"]}, gimimo metai: {pet["birth_year"]}")
            print("Naujas vardas:")
            pet["name"] = input()
            print("Nauja rūšis:")
            pet["species"] = input()
            print("Nauji gimimo metai:")
            pet["birth_year"] = int(input())
            break
    save_pets(pets)

def remove_pet(pets):
    print("Augintinio šalinimas")
    print("Įveskite augintinio ID:")
    del_id = input()
    for pet in pets:
        if del_id == str(pet["id"]):
            print(f"Šalinamas: {pet["id"]}. {pet["name"]} – {pet["species"]}, gimimo metai: {pet["birth_year"]}")
            pets.remove(pet)
            break
    save_pets(pets)