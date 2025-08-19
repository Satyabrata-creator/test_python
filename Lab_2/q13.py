age = int(input("Enter your age: "))

if 0 <= age <= 12:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teenager"
elif 20 <= age <= 59:
    category = "Adult"
elif age >= 60:
    category = "Senior Citizen"
else:
    category = "Invalid age entered"

print("You are classified as:")
print(category)
