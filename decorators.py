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
        result_string = ""
        if len(result) == 0:
            raise Exception("No results found")
        else:
            for worker in result:
                result_string += f"{worker}\n"
        return result_string
    return wrapper
