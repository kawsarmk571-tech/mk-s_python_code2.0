age = int(input("Enter your age: "))

if age >= 18 and age < 60:
    print("You are an Adult")
elif age >= 60:
    print("You are a Senior Citizen")
else:
    print("You are a Minor")