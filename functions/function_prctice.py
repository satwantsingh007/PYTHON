def greet(name, location):
    print(f"Welcome {name}")
    print(f"to  {location}")

greet(name='harry', location='UK')

def repeat_iterable(a, n):
    factor = int(n / len(a) + 1)
    repeated_list = a * factor
    print(repeated_list[:n])

repeat_iterable([1, 2, 3], 10)
