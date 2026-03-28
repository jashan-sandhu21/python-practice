print("Welcome to love calculator!!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name_combined = name1 + name2
name_lower = name_combined.lower()
t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")
true = t + r + u + e
l = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")
love = l + o + v + e 
total = str(true)+ str(love) 
total_int = int(total)
if (total_int < 10) or (total_int > 90):
    print(f"Your score is {total_int}, you go together like coke and mentos. ")
elif (total_int >= 40) and (total_int <= 50):
    print(f"your score is {total_int}, you are alright together. ")
else:
    print(f"your score is {total_int}. ")
    