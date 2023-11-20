from Worker import Worker
import decorators
import csv

def id_generator():
    num = 1
    while num < 10**3:
        yield num
        num += 1

class Collection:
    def __init__(self):
        self.collection = []
        self.id_generator = id_generator()

    def read_from_csv(self):
        user_input = input("Enter file name: ")
        try:
            with open(user_input, newline = '') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    worker = Worker(row['name'], row['surname'], row['department'], row['salary'])
                    worker.set_id(next(self.id_generator))
                    self.collection.append(worker)
        except FileNotFoundError:
            print("File not found")
            return

    def delete_worker(self):
        user_input = int(input("Enter ID: "))
        for worker in self.collection:
            if worker.get_id() == user_input:
                self.collection.remove(worker)
                return
        raise ValueError("Worker not found")
    
    def add_worker(self):
        worker = Worker(
            input("Enter name: "),
            input("Enter surname: "),
            input("Enter department: "),
            input("Enter salary: ")
        )
        if not worker.salary.isnumeric() or int(worker.salary) < 0:
            raise ValueError("Salary must be positive number")
            return
        worker.set_id(next(self.id_generator))
        self.collection.append(worker)

    def edit_worker(self):
        user_input = int(input("Enter ID: "))
        choice = input("Field to edit\n1. Name \n2. Surname \n3. Department \n4. Salary\nEnter number: ")
        if choice not in ["1", "2", "3", "4"]:
            print("Wrong input")
            return
        paths = {
            "1": "name",
            "2": "surname",
            "3": "department",
            "4": "salary"
        }
        setattr(
            self.collection[user_input - 1],
            paths[choice],
            input("Enter new data: ")
        )

    def print_to_csv(self):
        user_input = input("Enter file name: ")
        with open(user_input, 'w', newline = '') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'surname', 'department', 'salary'])
            for worker in self.collection:
                writer.writerow({
                    'id': worker.get_id(),
                    'name': worker.name,
                    'surname': worker.surname,
                    'department': worker.department,
                    'salary': worker.salary
                })
    
    def print_workers(self):
        for worker in self.collection:
            print(worker)

    @decorators.sort_decorator
    def sort_workers(self, key):
        self.collection.sort(key = lambda x: getattr(x, key))
    
    @decorators.search_decorator
    def search_workers(self, key):
        return list(filter(lambda x: x.name.casefold() == key.casefold() 
                           or x.surname.casefold() == key .casefold()
                           or x.department.casefold() == key.casefold()
                           or x.salary.casefold() == key.casefold(),
                           self.collection))