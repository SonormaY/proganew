class Worker:
    def __init__(self, name, surname, department, salary):
        __id = 0
        self.name = name
        self.surname = surname
        self.salary = salary
        self.department = department

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
    
    def __str__(self):
        return f"[{self.get_id()}]{self.name} {self.surname}: {self.department}, {self.salary}"
    
    