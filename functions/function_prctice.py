def greet(name, location):
    print(f"Welcome {name}")
    print(f"to  {location}")
greet(name = 'harry', location='UK')

def repeat_iterable(a, N):
    factor = int(N / len(a) + 1)
    repeated_list = a * factor
    print(repeated_list[:N])
repeat_iterable([1,2,3],10)


