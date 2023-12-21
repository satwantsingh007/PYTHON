x = int(input("Enter First Number = "))
y = int(input("Enter Second Number = "))
add=(x+y)
subtract=(x-y)
multiply=(x*y)
division=(x/y)
h=input('which operation = ')
if h == 'add' :
    print(add)
elif h == 'subtract':
    print(subtract)
elif h == 'multiply':
    print(multiply)
else:
    print(division)
