import random


#1Initial messages.

input("PC: Welcome to the game!")
input("PC: Lets see how much mental power do you have ;)")
input("PC: I'll think about a number. Eeeeeehhmmmm...let me see..")
input("PC: Could you wait a lil biit....PLLEEEEEASEEE!!!! >:x")
input("PC: OK..OK.. GOT IT! GOT IT!!")
input("PC: You have three choices...Good luck")

pc_numer = random.randint(1,100)
user_won = False

 
user_numer = 0
ini = 1
end = 4
for i in range(ini,end):
    print(f"ROUND {i}*****")
    user_numer = int(input(f"This is your {i} attempt. INPUT HERE YOUR NUMBER:"))
    input("PC: Are you sure?") #We can insert a yes and no later
    if user_numer > pc_numer:
        input("One step to death...and above my number.")
        input(f"TRY AGAIN! YOU HAVE {end-i} oportunitties more!")
        print("*********************")
    elif user_numer < pc_numer:    
        input("An opportunity less. Your live is low of time, as your number.")
        input(f"TRY AGAIN! YOU HAVE {end-i} opportunities more!")
        print("*********************")
    else:
        input("YOU ARE A MASTER! YOU WON")
    print("END OF THE GAME")
    print("*********************")
            
#There is a corruption between while and for loops. So its on my own to choose if the game
#have 3 opportunities or it will continue to until usr wins.