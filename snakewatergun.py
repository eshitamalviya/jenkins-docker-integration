import random
guess = 0
cscore = 0
uscore = 0
q=0

def functionname():
    pass

while(1):
 choiceuser = input("Enter your choice from -> snake, water, gun\n")
 if 0<=guess<=4:
  if  choiceuser=="snake":
    choice = random.choice([ "water", "gun"])
    guess += 1
    if choice=="water":
        print(f"COMPUTER CHOSE {choice}\n*****YOU WIN!!*****\nGuess left {5-guess}")
        uscore += 1

    else:
        print(f"COMPUTER CHOSE {choice}\n*****COMPUTER WINS!!*****\nGuess left {5-guess}")
        cscore += 1

  if choiceuser=="water":
    choice = random.choice(["snake", "gun"])
    guess += 1
    if choice == "snake":
        print(f"COMPUTER CHOSE {choice}\n*****COMPUTER WINS!!*****\nGuess left {5-guess}")
        cscore += 1
    else:
        print(f"COMPUTER CHOSE {choice}\n*****YOU WIN!!*****\nGuess left {5-guess}")
        uscore += 1
  if choiceuser=="gun":
    choice = random.choice(["snake","water"])
    guess += 1
    if choice == "snake":
        print(f"COMPUTER CHOSE {choice}\n*****YOU WIN!!*****\nGuess left {5-guess}")
        uscore += 1
    else:
        print(f"COMPUTER CHOSE {choice} \n*****COMPUTER WINS!!*****\nGuess left {5-guess}")
        cscore += 1

  if guess==5 :
    print(f"Game Over\nYour Score = {uscore}\nComputer's score = {cscore}")
    if cscore>uscore:
        guess=0
        print("COMPUTER HAS WON THIS SERIES\nWant to Play Again Press 1 for YES and 0 for NO???")
        q=int(input("YES OR NO??"))
        if q == 0:
            break
        if q == 1:
            continue
    if cscore<uscore:
        guess=0
        print("YOU HAVE WON THIS SERIES\nWant to Play Again Press 1 for YES and 0 for NO ???")
        q = int(input("YES OR NO??"))
        if q == 0:
            break
        if q == 1:
            continue




