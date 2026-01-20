from file_CRUD import *

# MY PETS CRUD (id, name, species, birth_year)

while True:
    print_info()
    įvestis = input()
    match įvestis:
        case "1":
            print_pets()
        case "2":
             create_pet()
        case "3":
            edit_pet()
        case "4":
            remove_pet()
        case "5":
            print("Išeinama iš programos")
            break