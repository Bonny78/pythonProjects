import random
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
game_image=[rock, paper, scissors]

#asking user choice
user_choice=int(input("what do you want to choose. Type 0 for Rock, 1 for Paper or 2 for Scissors"))
computer= random.randint(0,2) #random pick by computer

if user_choice<0 or user_choice>2:
    print("You typed invalid number. You lose")
else:
    print(game_image[user_choice])
    print("Computer chose:")
    print(game_image[computer])

    if (user_choice==1 and computer==0) or (user_choice==0 and computer==2) or (user_choice==2 and computer==1):
        print("You win")
    elif (user_choice==1 and computer==1) or (user_choice==0 and computer==0) or (user_choice==2 and computer==2):
        print("Draw")
    else:
        print("You lose")