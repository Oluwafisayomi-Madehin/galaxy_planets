package main

import (
	"fmt"
	"math/rand"
	"regexp"
	"strconv"
)

var alphaRegex = regexp.MustCompile(`^[a-zA-Z]*$`)
var numericRegex = regexp.MustCompile(`^[0-9]*$`)

func isAlpha(s string) bool {
	return alphaRegex.MatchString(s)
}

func isNumeric(s string) bool {
	return numericRegex.MatchString(s)
}

func main() {
    userName := ""
	var inputValid bool
	attempts := 3
	var inputedNumberStr string
	randomNumber := rand.Intn(2500 - 1000) + 1000
	randomNumberStr := strconv.Itoa(randomNumber)

	for (len(userName) > 10 || len(userName) < 2) || !isAlpha(userName) {
		fmt.Println("Enter your name: ")
		fmt.Scanln(&userName)
	}

	fmt.Print("Welcome: " + userName)

	planets := [4]string{"Deuteron","Axton","Capricon","Galaticon"}
	fmt.Println("Choose a planet between in the order 0,1,2,3")
	userPlanetStr := "99"
	userPlanet, _ := strconv.Atoi(userPlanetStr)

	for (userPlanet < 0 || userPlanet > 3) || !isNumeric(userPlanetStr) {
		fmt.Println("Enter your planet. Choose a planet between in the order 0,1,2,3: ")
		fmt.Scanln(&userPlanetStr)
		userPlanet, _ := strconv.Atoi(userPlanetStr)

		if !isNumeric(userPlanetStr) {
			userPlanetStr = "99"
			fmt.Println("User planet can only be 0,1,2 or 3! ")
		} else {
			if userPlanet >= 0 && userPlanet <= 3 {
				fmt.Println("Welcome to " + planets[userPlanet])
				break
			}
		}
	}

	for !inputValid && attempts > 0 {
		fmt.Println("Guess a number: ")
		fmt.Scanln(&inputedNumberStr)

		if !isNumeric(inputedNumberStr) {
			inputedNumberStr = "999"
			fmt.Println("Invalid Character! This field can only take numeric values.")
        	fmt.Println("Reverting to default...")
		}

		inputedNumber, _ := strconv.Atoi(inputedNumberStr)

		if inputedNumber <= 1000 {
			inputValid = false
			fmt.Println("Too little!")
		} else if inputedNumber > 1000 && inputedNumber < 2500 {
			inputValid = true

			if inputedNumber <= randomNumber {
				fmt.Println("You lose!")
			} else if inputedNumber > randomNumber {
				fmt.Println("You win!")
			}

			fmt.Println("You prepared " + randomNumberStr + "!")
			break
		} else {
			inputValid = false
			fmt.Println("Too large!")
		}

		if attempts > 0 {
			attempts--
		} else {
			break
		}
	}

	if attempts <= 0 {
		fmt.Println("Gameover! Too many attempts.")
	}
}