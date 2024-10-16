import random 

def titleIntro():
    print("*"*40)
    print(" "*10,"GUESS THE NUMBER"," "*10)
    print("*"*40)

def playIt():
    numRam = random.randint(1,100)
    attempts = 0 #intentos
    while True:
        try:
            numUser = int(input("Enter a number from 1 to 100: "))
        except ValueError:
            print("Please, enter a valid number.")
            continue #el programa vuelva al comienzo del bucle while

        if numUser > numRam:
            attempts += 1
            print("The number is smaller, try again")

        elif numUser < numRam:
            attempts += 1
            print("The number is bigger, try again")
        else:
            attempts += 1
            print(f"Congratulations,you found the number. Was the {numRam}, en el intento {attempts}")
            break

titleIntro()
playIt()