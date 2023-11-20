
def sort_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Sorting Collection by {args[1]}...")
        try:
            func(*args, **kwargs)
        except AttributeError as e:
            print(f"Wrong input! {e}")
    return wrapper

def search_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Searching Collection for {args[1]}")
        result = func(*args, **kwargs)
        if len(result) == 0:
            print("No results")
        else:
            for worker in result:
                print(worker)
    return wrapper
