import random


range_num = int(input("What number is the maximum I can think of? "))
x = range_num
comp_number = random.randint(1,x)

gamemode = int(input("Press [1] to give your own turns or press [2] for game difficulty selection: "))
if gamemode == 1:
    turns = int(input("How many tries do you want to get? "))
    if turns <= 5:
        print("You are going crazy! That is gonna be hard man!")
        while turns > 0:
            guess = int(input(f"I thought of a number. Make a guess, you have {turns} turns left: "))
            if guess == comp_number:
                print(f"Yeah! The correct number is truly {comp_number}!")
                break
            elif guess > comp_number:
                print("Sorry, the number is smaller than that")
                turns -= 1
            elif guess < comp_number:
                print("Sorry, the number is bigger than that than that")
                turns -= 1
    elif turns > 5 and turns <= 10:
        print("All right, let's start")
        while turns > 0:
            guess = int(input(f"I thought of a number. Make a guess, you have {turns} turns left: "))
            if guess == comp_number:
                print(f"Yeah! The correct number is truly {comp_number}!")
                break
            elif guess > comp_number:
                print("Sorry, the number is smaller than that")
                turns -= 1
            elif guess < comp_number:
                print("Sorry, the number is bigger than that than that")
                turns -= 1
    elif turns > 10:
        print("Isn't that too easy for you?")
        while turns > 0:
            guess = int(input(f"I thought of a number. Make a guess, you have {turns} turns left: "))
            if guess == comp_number:
                print(f"Yeah! The correct number is truly {comp_number}!")
                break
            elif guess > comp_number:
                print("Sorry, the number is smaller than that")
                turns -= 1
            elif guess < comp_number:
                print("Sorry, the number is bigger than that than that")
                turns -= 1

elif gamemode == 2:
    difficulty = int(input("Choose difficulty: Easy [1], Medium [2], Hard [3]: "))
    if difficulty == 1:
        turns = 15
        while turns > 0:
            guess = int(input(f"I thought of a number. Make a guess, you have {turns} turns left: "))
            if guess == comp_number:
                print(f"Yeah! The correct number is truly {comp_number}!")
                break
            elif guess > comp_number:
                print("Sorry, the number is smaller than that")
                turns -= 1
            elif guess < comp_number:
                print("Sorry, the number is bigger than that than that")
                turns -= 1
    elif difficulty == 2:
        turns = 10
        while turns > 0:
            guess = int(input(f"I thought of a number. Make a guess, you have {turns} turns left: "))
            if guess == comp_number:
                print(f"Yeah! The correct number is truly {comp_number}!")
                break
            elif guess > comp_number:
                print("Sorry, the number is smaller than that")
                turns -= 1
            elif guess < comp_number:
                print("Sorry, the number is bigger than that than that")
                turns -= 1
    elif difficulty == 3:
        turns = 5
        while turns > 0:
            guess = int(input(f"I thought of a number. Make a guess, you have {turns} turns left: "))
            if guess == comp_number:
                print(f"Yeah! The correct number is truly {comp_number}!")
                break
            elif guess > comp_number:
                print("Sorry, the number is smaller than that")
                turns -= 1
            elif guess < comp_number:
                print("Sorry, the number is bigger than that than that")
                turns -= 1






