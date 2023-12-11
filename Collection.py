from hmac import new
from Worker import Worker
import decorators
import csv
import matplotlib.pyplot as plt

def id_generator():
    num = 1
    while num < 10**3:
        yield num
        num += 1

class Collection:
    def __init__(self):
        self.collection = []
        self.id_generator = id_generator()

    def read_from_csv(self, filename = None):
        if filename is None:
            filename = input("Enter file name: ")
        try:
            with open(filename, newline = '') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    worker = Worker(row['name'], row['surname'], row['department'], row['salary'])
                    worker.set_id(next(self.id_generator))
                    self.collection.append(worker)
        except FileNotFoundError:
            print("File not found")
            return

    def delete_worker(self, id = None):
        if id is None:
            id = int(input("Enter ID: "))
        for worker in self.collection:
            if worker.get_id() == id:
                self.collection.remove(worker)
                return
        raise ValueError("Worker not found")
    
    def add_worker(self, *args):
        worker = None
        if len(args) == 4:
            worker = Worker(*args)
        else:
            worker = Worker(
                input("Enter name: "),
                input("Enter surname: "),
                input("Enter department: "),
                input("Enter salary: ")
            )
        if not worker.salary.isnumeric() or int(worker.salary) < 0:
            raise ValueError("Salary must be positive number")
        worker.set_id(next(self.id_generator))
        self.collection.append(worker)

    def edit_worker(self, *args):
        if len(args) == 3:
            user_input = args[0]
            choice = args[1]
            new_data = args[2]
        else:
            user_input = int(input("Enter ID: "))
            choice = input("Field to edit\n1. name \n2. surname \n3. department \n4. salary\nEnter number: ")
            new_data = input("Enter new data: ")
        if choice not in ["name", "surname", "departament", "salary"]:
            raise Exception("Wrong input")
        paths = {
            "1": "name",
            "2": "surname",
            "3": "department",
            "4": "salary",
            "name": "name",
            "surname": "surname",
            "departament": "departament",
            "salary": "salary"
        }
        setattr(
            self.collection[user_input - 1],
            paths[choice],
            new_data
        )

    def print_to_csv(self, filename = None):
        if filename is None:
            filename = input("Enter file name: ")
        with open(filename, 'w', newline = '') as csvfile:
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

    def plot_workers(self):
        if len(self.collection) == 0:
            raise Exception("Collection is empty")
        department_counts = {}
        for worker in self.collection:
            department = worker.department
            if department in department_counts:
                department_counts[department] += 1
            else:
                department_counts[department] = 1
        
        departments = list(department_counts.keys())
        counts = list(department_counts.values())
        

        plt.pie(counts, labels=departments, autopct='%1.1f%%')
        plt.title("Workers by Department")
        plt.show()


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