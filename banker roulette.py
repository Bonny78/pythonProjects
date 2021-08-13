import random

name_string=input("Give me everybody's name separarted by a comma and space \n")
#converting into a list
name_list=name_string.split(", ")
#calculating length of the list
num_people=len(name_list)
#name is randomly picked
name_picked=name_list[random.randint(0,num_people-1)]

print(name_picked + " is going to buy the meal today!")