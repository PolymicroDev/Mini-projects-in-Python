import random
import webbrowser

def num_range(x,y):
    print(f"I have thought of a number between {x} and {y}")
    return random.randint(x,y)   
computer_number = num_range(1,15)

def difficulty(dif):
    match dif:
        case "easy":
            turn = 15
            return turn
        case "medium":
            turn = 10
            return turn
        case "hard":
            turn = 5
            return turn    
        case "impossible":
            turn = 1
            return turn

turn = difficulty("hard")
while turn != 0:
    guess = int(input(f"Make a guess, you have {turn} left: "))
    if guess > computer_number:
        print("Too high, sorry, try again")
        turn -= 1
    elif guess < computer_number:
        print("Too low, sorry, try again")
        turn -= 1
    elif turn == 0:
        print("You lose...") 
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        print(f"Yeah, the correct number is {computer_number}!")
        webbrowser.open("https://media3.giphy.com/media/9xt1MUZqkneFiWrAAD/giphy.gif?cid=ecf05e47kt1op7lofoxmysqqgxqgjwea64mi0bzpiogxugmn&rid=giphy.gif&ct=g")
        
