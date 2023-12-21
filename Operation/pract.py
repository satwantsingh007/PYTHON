'''
my_dict = {"name": "Ram", "age": 25}
new_dict = my_dict
new_dict["age"] = 37

print(my_dict)
print(new_dict)
'''

'''
a=[10,20,30]
b=[10,20,30]
print(id(a))
print(id(b))
print(a is b)
print(a==b)


x = input("Enter First Number = ")
y = input("Enter Second Number = ")
print(type(x))
print("Sum : ",x+y)
'''

#a,b,c = input("Enter 3 ages ").split()
#print(a)

#m = eval(input("Enter List : "))
#print(m)
#print(type(m))

'''
C = int(input("Enter the celcius temperature : "))
Fahrenhite = C*(9/5)+32
print(Fahrenhite)
'''
'''
a = input("Enter Word : ")
b = int(input("Enter number : "))
print(a*b)
'''
'''
b = int(input("Enter number : "))
if b%5 == 0 :
    print("It is divisible by 5 ")
else:
    print("not divisible by 5")
'''
'''
a = input("Enter Word : ")
c = list(a)
for x in c:
    if x in ['a','e','i','o','u']:
        d = c.count(x)
        d= d+1
        print("Number of vowels : ",d)
'''

'''
a = (input("Enter list : "))
b = a.split()
print("Max number : ",max(b))
print("Min number : ",min(b))
'''

'''
b = int(input("Enter number : "))
if b%b == 0 and b/1 == b:
    print("number")
'''

#from sys import argv
#print(type(argv))

'''
a,b,c = 25, "Sunny" , "Python"
print("My name is %s and age is %s and i am studying %d "%(b,c,a))
print("My name is {0} and age is {1} and i am studying {2} ".format(b,c,a))
'''
'''
b = int(input("Enter number : "))
if b%2 == 0:
    print("its even")
else:
    print("its odd")

for x in range(10):
    print(x)
'''
'''
list = (input("Enter list - ").split())
for x in list:
    print(list)
'''

"""
n = int(input("Enter - "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end='')
    print()
"""

'''
s = 'durga is \ a good sir'
print(s)
'''

#s = 'durga'
#s[:-1:]

'''
two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two integers together
two_digit_number = first_digit + second_digit

print(two_digit_number)
'''
'''
a = input()
b = input()
c = a +' '+ b
print("final - {0} {1}".format(a,b))
print(c)
print(type(c))
'''
'''
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

BMI = int(weight)/(float(height)*float(height))
print(BMI)
'''
'''
print("Welcome to roller coster")
height = int(input("Enter height in cm : "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input ("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
'''

'''
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t+r+u+e
l= lower_names.count("l")
o= lower_names.count("o")
v= lower_names.count("v")
e =lower_names.count("e")
second_digit = l+o+v+e
score= int(str(first_digit) + str(second_digit))
if (score < 10) or (score> 90):
  print (f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 500):
  print (f"Your score is {score}, you are alright together.")
else:
  print (f"Your score is {score}.")
'''

'''
print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice = input("Kindly select where you want to go either 'left' or 'right' ?")
if choice == "left":
    choice_2 = input("Kindly select whether you want to 'wait' for the boat or want to 'swim' to cross the island.")
    if choice_2 == "wait":
        choice_3 = input("Now you have three door to choose, 'red', 'blue','yellow'")
        if choice_3 == "red":
            print("Game over! you were burned by a fire.")
        elif choice_3 == "yellow":
            print("Congratulations, you won the treasure.")
        elif choice_3 == "blue":
            print("Game over! you were eaten by beasts.")
        else:
            print("Game over.")
    else:
        print("Game over! you are attacked by a trout.")
else:
    print("Game Over! You fall into a hole.")

'''





