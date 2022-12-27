userName = input("Enter your name: ")
if len(userName) >= 10:
    print("Too much info - keep it shorter!")
else: 
    print("Welcome " + userName)

planets = ["Deuteron","Axton","Capricon","Galaticon"]
print("Choose a planet between Deuteron, Axton, Capricon, Galaticon in the order 0,1,2,3")

userPlanet = input("Enter your planet: ")
print("Welcome to " + planets[int(userPlanet)])