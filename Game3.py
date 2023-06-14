import time
import random

# a list which has two strings
li = ["forest", "dark cave"]
# to choose randomly from the list
choice = random.choice(li)
# the score which will increase at the game
score = 0

# story teller
def scene():
    print("Your Score: " + str(score) + "/10")
    print("The time is 20 o'clock.")
    time.sleep(1)
    print("You are in an open place and you are breething fresh air and you have a sword that made of gold in your hand to protect your self.")
    time.sleep(3)
    print("In front of you, you can see a " + choice +" inwhich there is a blue dragon that is danger and it is a big trouble.")
    time.sleep(3)
    print(" You can also see a small village that its habitants hates you and you are not wellcomed in this village. The individual in this village sleep at 22 o'clock. In this village you can find a gigantic and magic diamond sword.")
    time.sleep(7)
    print("Enter 1 to explore the " + choice)
    time.sleep(0.5)
    print("Enter 2 to get to the village")
    time.sleep(0.5)
    print("What would you like to do??")
    time.sleep(0.5)

# actions which happens at the dark cave or forest
def cave_or_forest():
    time.sleep(0.5)
    print("You are walking into the " + choice + ".")
    time.sleep(1.0)
    print("OH..NOOO!!")
    time.sleep(1.5)
    print("It is the blue dragon !!")
    time.sleep(0.5)
    print("Would you like to (1) fight the blue dragon with the golden sword (2) escape from the " + choice)
    time.sleep(0.5)
    input1 = int(input("(Please enter one choice only 1 or 2)"))
    if input1 == 1:
        print("You are fighting the blue dragon..")
        time.sleep(1)
        print("You have just decided to use your sword")
        time.sleep(1)
        print("The blue dragon is stronger than you but you are still trying to kill it.")
        time.sleep(1)
        print("Unfortunately, the blue dragon breathes flames on you.")
        time.sleep(1)
        print("You couldn't edure. You Have Been Killed. ")
        time.sleep(1)
        print("Score: " + str(score+3)+ "/10")
        time.sleep(2)
        print("GAME OVER!! Do you want to play again please enter? (y/n)")
        y_or_n()
    
    elif input1 == 2:
        time.sleep(0.5)
        print("You survived !!")
        time.sleep(0.5)
        print("Score: " + str(score+2)+ "/10")
        time.sleep(2)
        print("You have just escaped from the " + choice + ".")
        time.sleep(0.5)
        print("Would you like to get into the: " + choice + " enter(1), village enter(2)")
        x = int(input("(Please enter one choice only 1 or 2)"))
        if input1 == 1:
            cave_or_forest()
        elif input1 == 2:
            village()
                
# actions which happens in the village
def village():
    time.sleep(0.5)
    print("You are walking into the village.")
    time.sleep(1.0)
    print("If you like to get into the village, enter(1) for now, enter(2) for getting into it after midnight")
    time.sleep(0.5)
    input2 = int(input("(Please enter one choice only 1 or 2)"))
    if input2 == 1:
        print("You are walking into the village")
        time.sleep(1)
        print("The villagers have seen you.")
        time.sleep(1)
        print("Unfortunately, they could catch you.")
        time.sleep(1)
        print("Score: " + str(score+4)+ "/10")
        time.sleep(2)
        print("GAME OVER!! Do you want to play again please enter? (y/n)")
        y_or_n()
    elif input2 == 2:
        print("you are walking into the village after midnight")
        time.sleep(1)
        print("Fortunately, the villagers are sleeping now.")
        time.sleep(2)
        print("You have taken the magic sword.")
        time.sleep(1)
        print("Score: " + str(score+7)+ "/10")
        time.sleep(2)
        print("someone is coming !!")
        time.sleep(1)
        print("If you like to: go to the " + choice + " enter(1)," + " stay in the village enter(2).")
        time.sleep(0.5)
        input3 = int(input("(Please enter one choice only 1 or 2)"))
        if input3 == 2:
            print("A villager could catch you.")
            print("Score: " + str(score+8)+ "/10")
            print("GameOver, whould you like to play again ??(y/n)")
            y_or_n()
        elif input3 == 1:
            print("You are walking into the " + choice)
            time.sleep(1)
            print("OHHH...!! It's the blue dragon")
            time.sleep(1)
            print("would you like to use the old sword ==> enter(1), the new one ==> enter(2)")
            input4 = int(input("(Please enter one choice only 1 or 2)"))
            if input4 == 1:
                print("The blue dragon is stronger than you but you are still trying to kill it.")
                time.sleep(1)
                print("Unfortunately, the blue dragon breathes flames on you.")
                time.sleep(1)
                print("You couldn't edure. You Have Been Killed. ")
                time.sleep(1)
                print("Score: " + str(score+8.5)+ "/10")
                time.sleep(2)
                print("GAME OVER!! Do you want to play again please enter? (y/n)")
                y_or_n()
            elif input4 == 2:
                print("You are using the new sword")
                time.sleep(1)
                print("The dragon trying to overcome you, but you are stronger than it.")
                time.sleep(2)
                print("Fortunately, you could hit the target towards its head and finaly you could survive.")
                print("Congratulations!! You have won the game !!")
                time.sleep(1)
                print("Score: " + str(score+10)+ "/10")
                time.sleep(2)
                print("Do you want to play again?? (y/n)")
                y_or_n()
    else:
        print("(Please enter one choice only 1 or 2)")

while True:
    def y_or_n():
        while True:
            # this string to make sure if the result is 1 or 2
            let = str(input("(Please enter one choice y or n)"))
            
            # this statement to restart the game
            if let == "y":
                choice_check()
            
            # this statement to exit the game
            elif let == "n":
                print("Thanks For Playing Our Game!!")
                return
            
            # this statement to tell the user about his input if it was true or false
            else:
            	print("(Please enter one choice only y or n)")
    def choice_check():
        # story teller
        scene()
        
        # this variable to make sure from input
        input1 = int(input("(Please enter one choice only 1 or 2)"))
        
        # this statement to enable the "def cave_or_forest()"
        if input1 == 1:
            cave_or_forest()
            
        # this statement to enable the "def village()"
        elif input1 == 2:
            village()
            
        # this statement to tell the user to enter one choice only 1 or 2
        else:
            print("(Please enter one choice only 1 or 2)")
    
    # enable the "def choice_check()"
    choice_check()
