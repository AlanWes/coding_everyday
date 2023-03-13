import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

lenght_list = len(names)

random_number = random.randint(0, lenght_list - 1)

print(names[random_number] + " is going to buy the meal today!")