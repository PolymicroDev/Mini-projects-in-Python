import random

dic = {}
x = int(input("How many films do you want to add? "))
for i in range(x):
    film = input(f"{i+1}. film: ")
    dic[film] = input("The actor: ")


random_actor = random.choice(list(dic.values()))

print("The movies are the following: ")
for i in dic:
    print(f"-{i}")

for i in range(5):
    for title in dic:
        random_actor = random.choice(list(dic.values()))
        guess = input(f"Which film starred {random_actor} ")
        if dic[title] == random_actor:
            if guess == title:
                print("Correct!")
            print("Sorry, it is not correct")
        
       
        


    

        


