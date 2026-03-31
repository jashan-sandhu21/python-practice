import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
rps= [ rock,paper,scissors]
user = int(input("what do you chose? type 0 for rock , 1 for paper , 2 for scissors\n"))
if user >=3 or user < 0:
    print("invalid number.you lose!")
else:
    print(f"user chose:{user}")
    print (rps[user])
computer_chose = random.randint(0,2)
print(f"computer chose {computer_chose}")
print(rps[computer_chose])
if user >=3 or user < 0:
    print("invalid number.you lose!")
elif user == 0 and computer_chose == 0:
    print("It's a draw!")
elif user == 0 and computer_chose == 2:
    print("you win!!")
elif computer_chose > user:
    print("you lose!")
elif computer_chose == 0 and user == 2:
    print("you lose!")
elif user > computer_chose:
    print("you win!")
