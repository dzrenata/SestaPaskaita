                                     # MY PETS CRUD (id, name, species, birth_year)

pets = [
    {
        "id": 1,
        "name": "Vanilė",
        "species": "šuo",
        "birth_year": 2014
    },
    {
        "id": 2,
        "name": "Karamelė",
        "species": "triušis",
        "birth_year": 2023
    },
    {
        "id": 3,
        "name": "Lakis",
        "species": "vėžlys",
        "birth_year": 2025
    }
]

id_counter = 3

while True:
    print("------------------------------------------------------------")
    print("1. Atvaizduoti augintinius")
    print("2. Pridėti augintinį")
    print("3. Redaguoti augintinį")
    print("4. Šalinti augintinį")
    print("5. Išeiti iš programos")
    print("---------------------- Pasirinkite: -------------------------")

    įvestis = input()

    match įvestis:
        case "1":
            print("Augintinių sąrašas:")
            for pet in pets:
                print(f"{pet["id"]}. {pet["name"]} – {pet["species"]}, gimimo metai: {pet["birth_year"]}")

        case "2":
            print("Augintinio pridėjimas")
            print("Įveskite vardą:")
            name = input()
            print("Įveskite rūšį:")
            species = input()
            print("Įveskite gimimo metus:")
            birth_year = int(input())
            id_counter += 1
            pet = {
                "id": id_counter,
                "name": name,
                "species": species,
                "birth_year": birth_year
            }
            pets.append(pet)

        case "3":
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

        case "4":
            print("Augintinio šalinimas")
            print("Įveskite augintinio ID:")
            del_id = input()
            for pet in pets:
                if del_id == str(pet["id"]):
                    print(f"Šalinamas: {pet["id"]}. {pet["name"]} – {pet["species"]}, gimimo metai: {pet["birth_year"]}")
                    pets.remove(pet)
                    break

        case "5":
            print("Išeinama iš programos")
            break
