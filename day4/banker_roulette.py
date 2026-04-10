import random 
names = input("Give me everybody's name separated by commas. ")
name = names.split(",")
print(name)
total_persons = len(name)
bill = random.randint(0,total_persons-1)
person_who_will_pay = name[bill]
print(person_who_will_pay + "will pay the bill.")

