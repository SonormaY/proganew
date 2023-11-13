from Collection import Collection
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear') 

workers = Collection()
while True:
    clear()
    print("1. Print workers")
    print("2. Add worker")
    print("3. Delete worker")
    print("4. Edit worker")
    print("5. Sort workers")
    print("6. Search workers")
    print("7. Read CSV")
    print("8. Print CSV")
    print("0. Exit")
    n = input("Enter number:")
    if n == "1":
        workers.print_workers()
        input("Press enter to continue...")
    elif n == "2":
        workers.add_worker()
    elif n == "3":
        workers.delete_worker()
    elif n == "4":
        workers.edit_worker()
    elif n == "5":
        workers.sort_workers(input("Enter field to sort: "))
        input("Press enter to continue...")
    elif n == "6":
        workers.search_workers(input("Enter value to search: "))
        input("Press enter to continue...")
    elif n == "7":
        workers.read_from_csv()
    elif n == "8":
        workers.print_to_csv()
    elif n == "0":
        exit(1)
    else:
        print("Wrong input")