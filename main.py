from listCrud import *
# MY PETS CRUD (id, name, species, birth_year)

pets = load_default_data()

id_counter = 3

while True:
    print_info()
    įvestis = input()
    match įvestis:
        case "1":
            print_pets(pets)
        case "2":
            id_counter = create_pet(pets, id_counter)
        case "3":
            edit_pet(pets)
        case "4":
            remove_pet(pets)
        case "5":
            print("Išeinama iš programos")
            break
