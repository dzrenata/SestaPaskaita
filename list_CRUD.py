from list_demo_data import load_pets
id_counter = 3
pets = load_pets()

def print_info():
    print("------------------------------------------------------------")
    print("1. Atvaizduoti augintinius")
    print("2. Pridėti augintinį")
    print("3. Redaguoti augintinį")
    print("4. Šalinti augintinį")
    print("5. Išeiti iš programos")
    print("---------------------- Pasirinkite: -------------------------")

def print_pets():
    for pet in pets:
        print(f"{pet["id"]}. {pet["name"]} – {pet["species"]}, gimimo metai: {pet["birth_year"]}")

def create_pet():
    print("Augintinio pridėjimas")
    print("Įveskite vardą:")
    name = input()
    print("Įveskite rūšį:")
    species = input()
    print("Įveskite gimimo metus:")
    birth_year = int(input())
    global id_counter
    id_counter += 1
    pet = {
        "id": id_counter,
        "name": name,
        "species": species,
        "birth_year": birth_year
    }
    pets.append(pet)

def edit_pet():
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

def remove_pet():
    print("Augintinio šalinimas")
    print("Įveskite augintinio ID:")
    del_id = input()
    for pet in pets:
        if del_id == str(pet["id"]):
            print(f"Šalinamas: {pet["id"]}. {pet["name"]} – {pet["species"]}, gimimo metai: {pet["birth_year"]}")
            pets.remove(pet)
            break