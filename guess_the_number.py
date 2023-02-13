import random


#1Initial messages.

input("Welcome to the game!")
input("Lets see how much mental power do you have ;)")
input("I'll think about a number. Eeeeeehhmmmm...let me see..")
input("Could you wait a lil biit....PLLEEEEEASEEE!!!! >:x")
input("OK..OK.. GOT IT! GOT IT!!")
input("You have three choices...Good luck")

pc_numer = random.randint(1,100)
user_won = False

while not user_won: #(user_won == False) -> not False is True   
    user_numer = 0
    for i in range(1,3):
        user_numer = int(input(f"This is your {i + 1} attempt. Choose wisely... "))
        input("Are you sure?") #We can insert a yes and no later
        if user_numer > pc_numer:
            input("One step to death...and above my number.")
            input(f"TRY AGAIN! YOU HAVE {i} OPPORTUNITIES MORE!")
        elif user_numer < pc_numer:    
            input("An opportunity less. Your live is low of time, as your number.")
            input(f"TRY AGAIN! YOU HAVE {i} OPPORTUNITIES MORE!")
        else:
            input("YOU ARE A MASTER! YOU WON")
            
            