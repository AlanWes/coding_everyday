import random
import os

program = 1
hp = 6

main_word_list = [
    'FULLMETALALCHEMIST', 'DEATHNOTE', 'COWBOYBEPOP', 'SPIRITEDAWAY',
    'PRINCESSMONONOKE', 'ELFENLIED', 'BLEACH', 'NARUTO', 'EVANGELION'
]

#random word and empty blanks
random_word = main_word_list[random.randint(0, 8)]

main_word_letters = list(random_word)

len_random_word = len(random_word)

empty_list = []
for empty in range(len_random_word):
    empty = empty_list.append("_")

while program == 1:
    program = 0
    command = 'cls'
    count = -1

    if hp == 6:
        print('''
  +---+
  |   |
      |
      |
      |
      |
''')
    elif hp == 5:
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
''')
    elif hp == 4:
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
''')
    elif hp == 3:
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
''')
    elif hp == 2:
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
''')
    elif hp == 1:
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
''')
    elif hp == 0:
        print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
''')

    if "_" not in empty_list:
        print(f"\nYou are genius, main word is {random_word}. You win! :)")
        break

    for i in empty_list:
        print(i, end=" ")

    #ask player, check the blanks and replace

    p_letter = input("\n\nGuess a letter: ").upper()

    for letter in random_word:
        count += 1
        if p_letter == letter:
            empty_list[count] = main_word_letters[count]

    if p_letter not in empty_list:
        print(f"\n{p_letter} is not in the main word!")
        hp -= 1
        if hp == 0:
            print(f"You loose! Main word is {p_letter}")
            break
        input(f"\nClick ENTER to continue, you have left {hp} hp.")


    os.system(command)
    program += 1
