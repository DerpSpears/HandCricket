import random
def main():
    wickets=int(input("Till How many wickets are we playing? "))
    print("From This point on input only numbers b/w 1 and 6")
    while True:
        batorball=int(input("Give Number for Choice of batting or balling : "))
        if batorball>6:
            continue
        compbatorball=random.randint(1,6)
        print("Computer:",compbatorball)
        if compbatorball>batorball:
            cchoice=random.choice(["bat","ball"])
            match cchoice:
                case "bat":
                    hchoice="ball"
                case "ball":
                    hchoice="bat"
            break
        elif compbatorball<batorball:
            hchoice=input("bat or ball ? ").strip().lower()
            match hchoice:
                case "bat":
                    cchoice="ball"
                case "ball":
                    cchoice="bat"
            break
        else:
            continue
    game=0
    sgame={"human" : 0 , "computer" : 0}
    score=0
    while game!=2:
        print("Computer :",cchoice)
        print("Human :",hchoice)
        checkwick=0
        while checkwick!=wickets:
            hnum=int(input("Your Move : "))
            if hnum>6:
                print("Stop Trying to cheat")
                continue
            cnum=random.randint(1,6)
            print("Computer's Move :",cnum)
            if cnum==hnum:
                print("Out")
                checkwick=checkwick+1
            else:
                match hchoice:
                    case "ball":
                        score=score+cnum
                        continue
                    case "bat":
                        score=score+hnum
                        continue
        game=game+1
        if hchoice=="bat":
            sgame["human"]=score
            hchoice="ball"
            cchoice="bat"
        else:
            sgame["computer"]=score
            cchoice="ball"
            hchoice="bat"
    if(sgame["human"]>sgame["computer"]):
        print("Human wins with score :",sgame["human"],"-",sgame["computer"])
    else :
        print("Computer Wins with score :" , sgame["computer"],"-",sgame["human"])
main()






