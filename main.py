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
    print("5. Read CSV")
    print("6. Print CSV")
    print("7. Exit")
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
        workers.read_from_csv()
    elif n == "6":
        workers.print_to_csv()
    elif n == "7":
        exit(1)
    else:
        print("Wrong input")