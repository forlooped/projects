import time
score=0

name=str(input("Who dares to accept this challenge? \n"))
print("Welcome, "+name+", get ready...\n")
time.sleep(.5)
print("Here we go!\n")

def scoreAdd():
    global score
    score += 1
    print("score: ",score," \n")

def scoreBoo():
    global score
    score -= 1
    print("score: ",score," \n")

def q1():
    global score
    print("1. what color is purple?")
    print("a. pink")
    print("b. purple")
    print("c. blue")
    print("d. silver\n")

    answer = str(input("Answer: "))
    time.sleep(1)
    if answer == "b":
        print("Yay! That's right! purple is purple!")
        scoreAdd()
        
    else:
        print("Sorry. Answer is b: purple is purple")
        scoreBoo()
        
    q2()
        
def q2():
    global score
    print("1. which is an animal?")
    print("a. flower")
    print("b. door")
    print("c. bug")
    print("d. dog\n")

    answer = str(input("Answer: "))
    time.sleep(1)
    if answer == "d":
        print("Yay! Yes, a dog is an animal!")
        scoreAdd()
        
    else:
        print("Whoops, A dog is an animal. Answer is d")
        scoreBoo()
        
    q3()

def q3():
    global score
    print("1. what 5?")
    print("a. napkin")
    print("b. couch")
    print("c. number")
    print("d. tree\n")

    answer = str(input("Answer: "))
    time.sleep(1)
    if answer == "c":
        print("Yay! That's right! 5 is a number!")
        scoreAdd()        
        
    else:
        print("No, 5 is a number. Answer is c\n")
        scoreBoo()       
        
    time.sleep(1)
    print("Thank you for playing, "+name)

q1()
