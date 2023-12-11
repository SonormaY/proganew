from Collection import Collection
from os import system, name
import unittest
import tkinter as tk
from tkinter import messagebox


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear') 

workers = Collection()

def gui_menu():
    def print_workers():
        if len(workers.collection) == 0:
            messagebox.showerror("Print Workers Error", "No workers to print")
            return
        str_workers = ""
        for worker in workers.collection:
            str_workers += str(worker) + "\n"
        messagebox.showinfo("Workers", str_workers)

    def add_worker():
        def submit_worker():
            try:
                workers.add_worker(entry_name.get(),
                                entry_surname.get(),
                                entry_department.get(),
                                entry_salary.get())
            except ValueError as e:
                messagebox.showerror("Add Worker Error", str(e))
            worker_window.destroy()

        worker_window = tk.Toplevel(root)
        worker_window.title("Add Worker")

        label_name = tk.Label(worker_window, text="Name:")
        label_name.pack()

        entry_name = tk.Entry(worker_window)
        entry_name.pack()

        label_surname = tk.Label(worker_window, text="Surname:")
        label_surname.pack()

        entry_surname = tk.Entry(worker_window)
        entry_surname.pack()

        label_department = tk.Label(worker_window, text="Department:")
        label_department.pack()

        entry_department = tk.Entry(worker_window)
        entry_department.pack()

        label_salary = tk.Label(worker_window, text="Salary:")
        label_salary.pack()

        entry_salary = tk.Entry(worker_window)
        entry_salary.pack()

        button_submit = tk.Button(worker_window, text="Submit", command=submit_worker)
        button_submit.pack()

    def delete_worker():
        def submit_delete():
            id = entry_id.get()
            try:
                workers.delete_worker(int(id))
            except ValueError as e:
                messagebox.showerror("Delete Worker Error", str(e) + id)
            finally:
                messagebox.showinfo("Delete Worker", "Successfully deleted worker with ID " + id)
            delete_window.destroy()
        
        delete_window = tk.Toplevel(root)
        delete_window.title("Delete Worker")

        label_id = tk.Label(delete_window, text="ID:")
        label_id.pack()

        entry_id = tk.Entry(delete_window)
        entry_id.pack()

        button_submit = tk.Button(delete_window, text="Submit", command=submit_delete)
        button_submit.pack()

    def edit_worker():
        def submit_edit():
            try:
                workers.edit_worker(int(entry_id.get()), entry_field.get(), entry_new_data.get())
            except Exception as e:
                messagebox.showerror("Edit Worker Error", str(e))
            finally:
                messagebox.showinfo("Edit Worker", "Successfully edited worker with ID " + entry_id.get())
            edit_window.destroy()

        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Worker")

        label_id = tk.Label(edit_window, text="ID:")
        label_id.pack()

        entry_id = tk.Entry(edit_window)
        entry_id.pack()

        label_field = tk.Label(edit_window, text="Field:")
        label_field.pack()

        entry_field = tk.Entry(edit_window)
        entry_field.pack()

        label_new_data = tk.Label(edit_window, text="New Data:")
        label_new_data.pack()

        entry_new_data = tk.Entry(edit_window)
        entry_new_data.pack()

        button_submit = tk.Button(edit_window, text="Submit", command=submit_edit)
        button_submit.pack()
    
    def sort_workers():
        field = entry_sort.get()
        workers.sort_workers(field)
        messagebox.showinfo("Sort Workers", "Press OK to continue...")

    def search_workers():
        value = entry_search.get()
        messagebox.showinfo("Search Workers", workers.search_workers(value))

    def read_from_csv():
        try:
            workers.read_from_csv(entry_read_csv.get())
        except Exception as e:
            messagebox.showerror("Read from CSV Error", str(e))
        messagebox.showinfo("Read from CSV", "Press OK to continue...")

    def print_to_csv():
        workers.print_to_csv(entry_print_to_csv.get())
        messagebox.showinfo("Print to CSV", "Press OK to continue...")

    def plot_workers():
        try:
            workers.plot_workers()
        except Exception as e:
            messagebox.showerror("Plot Workers Error", str(e))

    def exit_program():
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            root.destroy()

    root = tk.Tk()
    root.title("Menu")

    label_title = tk.Label(root, text="Menu", font=("Arial", 16))
    label_title.pack(pady=10)

    button_print_workers = tk.Button(root, text="Print Workers", command=print_workers)
    button_print_workers.pack()

    button_add_worker = tk.Button(root, text="Add Worker", command=add_worker)
    button_add_worker.pack()

    button_delete_worker = tk.Button(root, text="Delete Worker", command=delete_worker)
    button_delete_worker.pack()

    button_edit_worker = tk.Button(root, text="Edit Worker", command=edit_worker)
    button_edit_worker.pack()

    label_sort = tk.Label(root, text="Sort Workers by Field:")
    label_sort.pack()

    entry_sort = tk.Entry(root)
    entry_sort.pack()

    button_sort_workers = tk.Button(root, text="Sort Workers", command=sort_workers)
    button_sort_workers.pack()

    label_search = tk.Label(root, text="Search Workers by Value:")
    label_search.pack()

    entry_search = tk.Entry(root)
    entry_search.pack()

    button_search_workers = tk.Button(root, text="Search Workers", command=search_workers)
    button_search_workers.pack()

    label_read_csv = tk.Label(root, text="CSV filename:")
    label_read_csv.pack()

    entry_read_csv = tk.Entry(root)
    entry_read_csv.pack()

    button_read_from_csv = tk.Button(root, text="Read from CSV", command=read_from_csv)
    button_read_from_csv.pack()

    label_print_to_csv = tk.Label(root, text="CSV filename:")
    label_print_to_csv.pack()

    entry_print_to_csv = tk.Entry(root)
    entry_print_to_csv.pack()

    button_print_to_csv = tk.Button(root, text="Print to CSV", command=print_to_csv)
    button_print_to_csv.pack()

    button_plot_workers = tk.Button(root, text="Draw Pie chart by departament", command=plot_workers)
    button_plot_workers.pack()

    button_exit = tk.Button(root, text="Exit", command=exit_program)
    button_exit.pack()

    root.mainloop()

def console_menu():
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
            print(workers.search_workers(input("Enter value to search: ")))
            input("Press enter to continue...")
        elif n == "7":
            workers.read_from_csv()
        elif n == "8":
            workers.print_to_csv()
        elif n == "0":
            break
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
        print("1. Run graphical menu")
        print("2. Run console menu")
        print("2. Run tests")
        print("0. Exit")
        n = input("Enter number:")
        if n == "1":
            gui_menu()
        elif n == "2":
            console_menu()
        elif n == "3":
            test = TestCollection()
            test.runtest()
        elif n == "0":
            exit(1)
        else:
            print("Wrong input")