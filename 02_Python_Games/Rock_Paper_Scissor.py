import random

choices=('r','p','s')
user_choice = input("Rock, Paper or Scissor? (r/p/s) : ").lower()
if user_choice not in choices:
    print("Invalid Input!")

computer_choice = random.choice(choices)
