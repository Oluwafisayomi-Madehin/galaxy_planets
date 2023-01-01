import random

userName = input("Enter your name: ")
if len(userName) >= 10:
    print("Too much info - keep it shorter!")
else: 
    print("Welcome " + userName)

planets = ["Deuteron","Axton","Capricon","Galaticon"]
print("Choose a planet between in the order 0,1,2,3")

userPlanet = input("Enter your planet: ")
print("Welcome to " + planets[int(userPlanet)])

randomNumber = random.randint(1000, 2500)
inputValid = False

def inputedNumber():
    inputedNumber = int(input("Guess a number: "))
    inputValidityChecker()
    return inputedNumber

def inputValidityChecker():
    if inputedNumber() <= 1000:
        inputValid = False
        print("Too little!")

    elif inputedNumber() > 1000 & inputedNumber() < 2500:
        inputValid = True
        if inputedNumber() <= randomNumber:
            print("You lose!")

        elif inputedNumber() < randomNumber:
            print("You win!")

        print(planets[int(userPlanet)] + " prepared " + str(randomNumber) + "!")

    else:
        print("Too large!")
        inputValid = False


while inputValid == False:
    inputedNumber()
    