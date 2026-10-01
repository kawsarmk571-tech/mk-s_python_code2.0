secret_password = "1234"
while True :
    user_input = input ("Enter password:")
    if user_input == secret_password :
        print ("Access Granted !")
        break 
    else :
        print ("wrong Password, try again!")