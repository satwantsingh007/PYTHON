# from turtle import (Turtle, Screen)
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("firebrick2")
# timmy.shapesize(3, 3, 8)
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmender"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
