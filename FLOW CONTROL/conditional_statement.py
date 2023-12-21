"""
Even or Odd:
Write a program that takes an integer as input and prints whether it's even or odd.
"""

# number = int(input("Enter the number you want to check whether it's is odd or even : "))
# if number%2 == 0:
#     print("It is even number.")
# else:
#     print("It is odd number.")


"""
Grade Calculator:
Create a program that takes a student's percentage as input and prints their corresponding 
grade (A, B, C, D, or F). 
Assume the following grading scale: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59).
"""

# percentage = float(input("Enter your percentage : "))
# if percentage >= 90 and percentage <= 100:
#     print("A grade")
# elif percentage >= 80 and percentage <= 89:
#     print("B grade")
# elif percentage >= 70 and percentage <= 79:
#     print("C grade")
# elif percentage >= 60 and percentage <= 69:
#     print("D grade")
# elif percentage >= 0 and percentage <= 59:
#     print("F grade")
# else:
#     print("It's wrong input")


"""
Number Comparison:
Write a program that takes two numbers as input and prints whether the first number is greater,
 smaller, or equal to the second number.
"""
# number_1 = int(input("Enter first number: "))
# number_2 = int(input("Enter second number :"))
# if number_1 == number_2:
#     print("Both number has equal value. ")
# elif number_1 > number_2:
#     print("First number is greater than Second number. ")
# else:
#     print("First number is smaller than Second number. ")


"""
Positive, Negative, or Zero:
Create a program that takes a number as input and prints whether it's positive, negative, 
or zero.
"""
# number = int(input("Enter number : "))
# if number < 0:
#     print("its negative")
# elif number == 0:
#     print("its zero")
# else:
#     print("its positive")

"""
Ticket Price Calculator:
Build a program that asks the user for their age and determines the cost of a movie ticket. 
If the person is under 12, the ticket costs $5; 
if they are between 12 and 18, the ticket costs $10; otherwise, the ticket costs $15
"""

# age = int(input("Enter your age: "))
# ticket_price = 0
# if age < 12:
#     ticket_price = 5
# elif age> 12 and age<18:
#     ticket_price = 10
# else:
#     ticket_price = 15
# print(f"Your ticket costs ${ticket_price}")

"""
Vowel or Consonant:
Write a program that takes a single character as input and prints 
whether it's a vowel or a consonant.
"""

# letter = input("enter a single chacter\n")[0].lower()
# vowel = ['a','e','i','o','u']
# if letter in vowel:
#     print("It is a vowel. ")
# else:
#     print("It is a consonent.")

"""
Largest of Three Numbers:
Create a program that takes three numbers as input and prints the largest among them.
"""

# a = int(input("first number\n"))
# b = int(input("second number\n"))
# c = int(input("third number\n"))
# if a>b and a>c:
#     print("First number is the largest number")
# elif b>c:
#     print("Second number is the largest number.")
# else:
#     print("Third number is the largest number.")

"""
User Authentication:
Write a simple user authentication program. 
Ask the user to enter a username and password, and then check 
if the entered credentials match predefined values.
"""

# username = input("Create username\n")
# password = input("Create password\n")
#
# login_username = input("Enter username\n")
# login_password = input("Enter password\n")
#
# if username == login_username and password == login_password:
#     print("Welcome.")
# else:
#     print("Kindly enter correct credentials")

"""
Time of Day Greeting:
Build a program that takes the current hour as input (in 24-hour format) and 
prints a greeting message based on the time of day (morning, afternoon, evening).
"""

from datetime import datetime
now = datetime.now()
time = now.strftime("%H")
current_time = int(time)
if current_time>5 and current_time<12:
    print("Good Morning")
elif current_time>12 and current_time<18:
    print("Good Afternoon")
else:
    print("Good night")

