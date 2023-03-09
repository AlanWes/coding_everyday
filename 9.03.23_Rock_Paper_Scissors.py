rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

def game():
  comp = [rock, paper, scissors]
  
  player = input("What do you choose? Rock 1, paper 2 or scissors 3. : ")
  player_choice = int(player)

  def play():
    print(f"{comp[player_choice - 1]}")
    
    random_int = random.randint(1, 3)

    print(f"Computer choose: {comp[random_int - 1]}")
    
    def win():
      print("You win!")
    
    def lose():
      print("You lose!")
    
    def draw():
      print("Draw!")

    if player_choice == 1 and random_int == 1:
      draw()
    if player_choice == 2 and random_int == 2:
      draw()
    if player_choice == 3 and random_int == 3:
      draw()
      
    if player_choice == 1 and random_int == 2:
      lose()
    if player_choice == 1 and random_int == 3:
       win()
      
    if player_choice == 2 and random_int == 3:
      lose()
    if player_choice == 2 and random_int == 1:
      win()
      
    if player_choice == 3 and random_int == 2:
      win()
    if player_choice == 3 and random_int == 1:
      lose()
    

  if player_choice >= 4 or player_choice < 0:
    print("invalid value, restart")
    game()
  else:
    play()

game()