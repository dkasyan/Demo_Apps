weight = 97
height = 1.85

def BMICalculating(weight, height):
    BMI = weight / (height ** 2)
    if BMI < 18.5:
        print(f"Your BMI is {BMI}, you are underweight")
    elif BMI < 25:
        print(f"Your BMI is {BMI}, your weight is normal")
    elif BMI < 30: 
        print(f"Your BMI is {BMI}, you are overweight")


BMICalculating(weight, height)