# # #Password Generator Project
# # import random
# # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# # symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# #
# # print("Welcome to the PyPassword Generator!")
# # nr_letters = int(input("How many letters would you like in your password?\n"))
# # nr_symbols = int(input(f"How many symbols would you like?\n"))
# # nr_numbers = int(input(f"How many numbers would you like?\n"))
# #
# # #Eazy Level
# # # password = ""
# #
# # # for char in range(1, nr_letters + 1):
# # #   password += random.choice(letters)
# #
# # # for char in range(1, nr_symbols + 1):
# # #   password += random.choice(symbols)
# #
# # # for char in range(1, nr_numbers + 1):
# # #   password += random.choice(numbers)
# #
# # # print(password)
# #
# # #Hard Level
# # password_list = []
# #
# # for char in range(1, nr_letters + 1):
# #   password_list.append(random.choice(letters))
# #
# # for char in range(1, nr_symbols + 1):
# #   password_list += random.choice(symbols)
# #
# # for char in range(1, nr_numbers + 1):
# #   password_list += random.choice(numbers)
# #
# # #print(password_list)
# # random.shuffle(password_list)
# # #print(password_list)
# #
# # password = ""
# # for char in password_list:
# #   password += char
# #
# # print(f"Your password is: {password}")
#
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
#
# # Use list comprehension to generate the list of coordinates
# # my_list = []
# # for i in range(x + 1):
# #     for j in range(y + 1):
# #         for k in range(z + 1):
# #             if i + j + k != n:
# #                 my_list.append([i,j,k])
#
#
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if i + j + k != n:
#                 print([i, j, k])
#
# # Print the list of coordinates
# # print(my_list)


#
# l = [1,2 ,5]
# # print(l*2)
# l.append('asdfgh')
# print(l)
#
# nested_list = [[1, 2, 3], ['a', 'b', 'c']]
# print(nested_list[0][1])  # Accessing an element in a nested list
# my_list = [1, 2, 3, 4]
# for element in my_list:
#     if element % 2 == 0:
#         my_list.remove(element)  # This can cause unexpected behavior
#     else:
#         continue
# print(my_list)
#
# numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers.sort()  # Sort in-place
# print(numbers)
# sorted_numbers = sorted(numbers)  # Create a sorted copy
# reversed_numbers = numbers[::-1]  # Reverse the list
# print(sorted_numbers)
# print(reversed_numbers)

#--------------------------------------------------------------------------------------



