import random
import os

program = 1

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

    for i in empty_list:
        print(i, end=" ")

    #ask player, check the blanks and replace

    p_letter = input("\n\nGuess a letter: ").upper()

    for letter in random_word:
        count += 1
        if p_letter == letter:
            empty_list.remove(empty_list[count])
            empty_list.insert(count, p_letter)
            #?????????????

    os.system(command)
    program += 1
