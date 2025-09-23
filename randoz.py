import random

def randomize (randnum):
    rd = random.random()
    global finalRan
    finalRan = randnum * rd
    intRan = int(finalRan)
    print (intRan)
