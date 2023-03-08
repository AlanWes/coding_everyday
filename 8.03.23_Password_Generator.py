#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_main = []
number_main = []
symbol_main = []

for random_letter in range(nr_letters):
  random_letter = random.choice(letters)
  letter_main += str(random_letter)

for random_number in range(nr_numbers):
  random_number = random.choice(numbers)
  number_main += str(random_number)

for random_symbol in range(nr_symbols):
  random_symbol = random.choice(symbols)
  symbol_main += str(random_symbol)

main_list_demo = [letter_main, number_main, symbol_main]
main_list = []

for lists in main_list_demo:
  for i in lists:
    main_list.append(i)

random.shuffle(main_list)

main = "".join(main_list)

print(main)