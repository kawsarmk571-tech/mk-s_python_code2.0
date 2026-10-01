secret_password ="asthetic77"

while True:
    user_input = input("Enter password: ")
    
    if user_input == secret_password:
        print("Access Granted!")
        break
    else:
        print("Wrong password, try again!\n")