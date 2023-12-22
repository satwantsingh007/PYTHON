# import random
#
# rand = random.randint(1,200)
# randin = random.random()
# print(randin*rand)
# print(rand)
# print(randin)


# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input()
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"
# print(f"{line1}\n{line2}\n{line3}")

# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")

#-------------------------------------------------------------------------------------
# import random
# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """
#
# paper = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """
#
# scissors = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
# comp_choice = random.randint(0,2)
#
# if user_choice == 0 and comp_choice == 1:
#     print(f"{rock}\n Computer choose:\n {paper}\n You loose.")
# elif user_choice == 0 and comp_choice == 2:
#     print(f"{rock}\n Computer choose:\n {scissors}\n You loose.")
# elif user_choice == 1 and comp_choice == 0:
#     print(f"{paper}\n Computer choose:\n {rock}\n You Win.")
# elif user_choice == 1 and comp_choice == 2:
#     print(f"{paper}\n Computer choose:\n {scissors}\n You loose.")
# elif user_choice == 2 and comp_choice == 0:
#     print(f"{scissors}\n Computer choose:\n {rock}\n You loose.")
# elif user_choice == 2 and comp_choice == 1:
#     print(f"{scissors}\n Computer choose:\n {paper}\n You win.")
# elif user_choice >=3:
#     print("invalid choice")
# else:
#     print(f"{user_choice}\n{comp_choice}\n match draw")


'''
Sum of Elements:
Write a program that calculates and prints the sum of all elements in a given list
'''

# a = [1,3,5,3,67,4556,34,67,43,65]
# c = 0
# for x in a:
#     c += x
#     x+=1
# print(c)

'''
List Reversal:
Create a function that takes a list as input and returns a new list 
with the elements reversed. Do this both with and without using the reverse() method.
'''

# a = input("Enter list : ").split(' ')
# print(a[::-1])
# b = a.reverse()
# print(a)

'''
Even Numbers:
Write a program that takes a list of numbers as input and creates a new list 
containing only the even numbers.
'''

# a = input("Enter numbers : ").split(' ')
# print(f"New list : {a}")
# b = []
# for x in a:
#     x= int(x)
#     if x%2 == 0:
#         x = str(x)
#         b.append(x)
#     else:
#         continue
# print(f"Updated list : {b}")

#----------------------------------------------------------------------------------------

'''
List Intersection:
Implement a function that takes two lists as input and returns a new list containing 
only the common elements between the two lists.
'''
# a = input("Enter First list : ").split(' ')
# b = input("Enter Second list : ").split(' ')
# c = []
# for x in a:
#     for y in b:
#         if x == y and x not in c:
#             c.append(x)
#         else:
#             continue
# print(f"New list : {c}")

#---------------------------------------------------------------------------------------------

'''
List Flattening:
Write a program that flattens a nested list (a list of lists) into a single list.
'''
# First method
# a = [1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10,[11,12,[13,14]]] ] ]
# b = []
# for x in a:
#     if type(x) == list:
#         for y in x:
#             if type(y) == list:
#                 for j in y:
#                     b.append(j)
#             else:
#                 b.append(y)
#     else:
#         b.append(x)
# print(b)

#Second method

# input list
# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10,[11,12,[13,14,[15,[16]]]]]]]
#
# # output list
# output = []
#
# # function used for removing nested
# # lists in python using recursion
# def reemovNestings(l):
# 	for i in l:
# 		if type(i) == list:
# 			reemovNestings(i)
# 		else:
# 			output.append(i)
#
#
# # Driver code
# print('The original list: ', l)
# reemovNestings(l)
# print('The list after removing nesting: ', output)

'''
Remove Duplicates:
Create a function that takes a list as input and returns a new list 
with the duplicate elements removed.
'''

# a= input("Enter list: ").split(' ')
# b = []
# for x in a:
#     if x not in b:
#         b.append(x)
#     else:
#         continue
# print(a)
# print(b)

'''
List Comprehension:
Use list comprehension to create a new list that contains 
the squares of the numbers in the given list.
'''

# a = input("Enter first list: ").split(' ')
# b = input("Enter second list: ").split(' ')
# c = []
# for x in a:
#     x=int(x)
#     for y in b:
#         y = int(y)
#         if x == y**2:
#             c.append(x)
#         elif y == x**2:
#             c.append(y)
#         else:
#             continue
# print(c)

'''
List Rotation:
Implement a function that rotates the elements of a list to the left by a 
specified number of positions.
'''
# a = ['sam', 12 , 234 , 432 , 'dear', 4567, 23]
# n = int(input("Enter number of position : "))
# test = a[n:]+a[:n]
# print(f"Original List : {a}")
# print(f"List after left rotation : {test}")

'''
Two Sum Problem:
Given a list of integers and a target sum, write a function that returns True 
if there are two numbers in the list that add up to the target sum.
'''

# a = [2,4,5,765,34,6, 3]
# b = 9
# for x in range(len(a)):
#     for j in range(1+x, len(a)):
#         if a[x] + a[j] == b:
#             print(f"These numbers {a[x]} and {a[j]} are equal to {b} ",True)
#         else:
#             continue

'''
Largest and Smallest Elements:
Write a program that finds and prints the largest and smallest elements in a given list.
'''

# numbers = [4, 7, 1, 9, 12, 5, 3, 234]
# largest = numbers[0]
# smallest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
#     elif num < smallest:
#         smallest = num
# print(f"The largest element in the list is: {largest}")
# print(f"The smallest element in the list is: {smallest}")

#----------------------------------------------------------------------------------------------
# Write your code here 👇
# for x in range(1,101):
#   if x%3 == 0 and x%5 == 0:
#     print("FizzBuzz")
#   elif x%5 == 0:
#     print("Buzz")
#   elif x%3 == 0:
#     print("Fizz")
#   else:
#       print(x)
#--------------------------------------------------------------------------------
# PASSWORD GENERATOR
#
# import random
# from random import sample
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# password_list = []
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")

