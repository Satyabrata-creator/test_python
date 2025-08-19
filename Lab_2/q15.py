weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal weight"
elif 25.0 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print("Your BMI is: }")
print(bmi)
print(category)