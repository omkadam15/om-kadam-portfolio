def add(a, b):
    return a - b  # error

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def get_first_element(lst):
    if not lst:
        return "Empty list"
    return lst[0]
