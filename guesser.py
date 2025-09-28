import randoz
import time
import termtools
print("Guessing game")
won = False
Tries = 0


basestart = randoz.randomize(32)
while won == False: 
    compare = int(input("Guess here:"))
    if Tries == 5:
        print("Max tries. Ending in 3 seconds")
        time.sleep(2)
        Tries = 0
        termtools.clearer("linux")
        quit()
    if compare == basestart:
        print("You Did it")
        won = True
    
    elif compare <= basestart:
        print("A little more")
        Tries = Tries + 1
    elif compare >= basestart:
        print("A little less")
        Tries = Tries + 1
    else:
        print("Glitch")