from Collection import Collection
from os import system, name
import unittest

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear') 

workers = Collection()
def menu():
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
            try:
                workers.add_worker()
            except ValueError as e:
                print(e)
                input("Press enter to continue...")
        elif n == "3":
            try:
                workers.delete_worker()
            except ValueError as e:
                print(e)
                input("Press enter to continue...")
        elif n == "4":
            try:
                workers.edit_worker()
            except Exception as e:
                print(e)
                input("Press enter to continue...")
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

class TestCollection(unittest.TestCase):

    def test_add_worker(self):
        self.workers.add_worker("John", "Smith", "IT", "1000")
        self.assertTrue(self.workers.collection[-1].name == "John")
        self.assertEqual(len(self.workers.collection), 11)

    def test_delete_worker(self):
        self.workers.delete_worker(2)
        self.assertEqual(len(self.workers.collection), 10)

    def test_edit_worker(self):
        self.workers.edit_worker(1, "name", "nigga")
        self.assertEqual(self.workers.collection[0].name, "nigga")

    def test_sort_workers(self):
        self.workers.sort_workers("name")
        self.assertEqual(self.workers.collection[0].name, "Daniel")

    def test_read_from_csv(self):
        self.workers.read_from_csv("test.csv")
        self.assertEqual(len(self.workers.collection), 15)

    def runtest(self):
        self.workers = Collection()
        self.workers.add_worker("John", "Doe", "IT", "1000")
        self.workers.add_worker("Jane", "Smith", "HR", "2000")
        self.workers.add_worker("Michael", "Johnson", "Finance", "3000")
        self.workers.add_worker("Emily", "Brown", "Marketing", "4000")
        self.workers.add_worker("Daniel", "Wilson", "Sales", "5000")
        self.workers.add_worker("Olivia", "Taylor", "IT", "6000")
        self.workers.add_worker("William", "Anderson", "HR", "7000")
        self.workers.add_worker("Sophia", "Martinez", "Finance", "8000")
        self.workers.add_worker("James", "Lopez", "Marketing", "9000")
        self.workers.add_worker("Isabella", "Garcia", "Sales", "10000")
        self.test_add_worker()
        self.test_delete_worker()
        self.test_edit_worker()
        self.test_sort_workers()
        self.test_read_from_csv()
        print("Tests completed successfully")
        input("Press Enter to continue...")

if __name__ == "__main__":
    while True:
        clear()
        print("1. Run menu")
        print("2. Run tests")
        print("0. Exit")
        n = input("Enter number:")
        if n == "1":
            menu()
        elif n == "2":
            test = TestCollection()
            test.runtest()
        elif n == "0":
            exit(1)
        else:
            print("Wrong input")