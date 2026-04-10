height = float(input("What's your height?(in m) "))
weight = float(input("What's your weight?(in kg) "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"your BMI is {bmi}, you are underweight. ")
elif bmi < 25:
    print(f"your BMI is {bmi}, you have normal weight. ")
elif bmi < 30:
    print(f"your BMI is {bmi}, you are overweight. ") 
elif bmi <35:
    print(f"your BMI is {bmi}, you are obese. ")
else:
    print(f"your BMI is {bmi}, you are clinically obese.")
    