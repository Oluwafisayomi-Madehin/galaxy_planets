import random

userName = ""

while (len(userName) > 10 or len(userName) < 2) or userName.isalpha() == False: 
    userName = input("Enter your name: ")
    
    if (len(userName) > 10 or len(userName) < 2) or userName.isalpha() == False: 
        print("Invalid username! Username should be between 2 and 10 alphabets.")

else: 
    print("Welcome " + userName)

planets = ["Deuteron","Axton","Capricon","Galaticon"]
print("Choose a planet between in the order 0,1,2,3")
userPlanet = "99" 

while (int(userPlanet) < 0 or int(userPlanet) > 3) or userPlanet.isnumeric() == False: 
    userPlanet = input("Enter your planet. Choose a planet between in the order 0,1,2,3: ")

    if userPlanet.isnumeric() == False:
        userPlanet = "99"
        print("User planet can only be 0,1,2 or 3!")
else:
    userPlanet = int(userPlanet)
    print("Welcome to " + planets[userPlanet])

randomNumber = random.randint(1000, 2500)
inputValid = False
attempts = 3
inputedNumber = ""

while inputValid == False and attempts > 0:
    inputedNumber = input("Guess a number: ")
    
    if inputedNumber.isnumeric() == False:
        inputedNumber = "999"
        print("Invalid Character! This field can only take numeric values.")
        print("Reverting to default...")

    if int(inputedNumber) <= 1000:
        inputValid = False
        print("Too little!")

    elif int(inputedNumber) > 1000 and int(inputedNumber) < 2500:
        inputValid = True

        if int(inputedNumber) <= randomNumber:
            print("You lose!")

        elif int(inputedNumber) > randomNumber:
            print("You win!")

        print(planets[userPlanet] + " prepared " + str(randomNumber) + "!")

    else:
        inputValid = False
        print("Too large!")
    
    attempts -= 1

else:
    if attempts <= 0:
        print("Gameover! Too many attempts.")