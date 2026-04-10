print("Welcome to treasure island.")
print("Your mission is to find the treasure.")

start = input("You are at a crossroad. Where do you want to go? Type  left or right? ").lower()
if start=='left':
    print("you come to a lake. There is an Island in the middle of the lake.")
    next = input("Type 'wait' to wait for the boat or Type 'swim' to swim across.")
    print (next)
    if next == "wait":
        print("You arrived at the Island unharmed. There is a house with 3 doors - red, yellow and blue. ")
        door = input("which door you choose? \n")
        if door == "yellow":
            print("You win!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")