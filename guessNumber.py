
import random
import math
import colorama as cl


""""
    STEPS TO FOLLOW

randomize number
take input from user
control if randomNumer > input random < input ? 
and tell player to guess up or down
decrease chanceLeft on every wrong guess

"""
print("----------------------------------------------------------------")
print(cl.Fore.YELLOW+"Enter zero(0) to exit!!!")
print(cl.Fore.YELLOW+"Enter only between 1-100")
print("----------------------------------------------------------------")

rand = math.ceil(random.random() * 100);
chanceLeft = 5;
while(True):
    guess = int(input(cl.Fore.WHITE+"Enter your number: "))
    if( 101 > guess > 0):
        chanceLeft -=1;

        if guess > rand :
            print(cl.Fore.WHITE+"--->try lower number!<----", end=" ");
        elif guess < rand :
            print(cl.Fore.WHITE+"--->try higher number<----", end=" ")
        elif guess == rand:
            print(cl.Fore.GREEN+"congratulation!!!")
            break;
        print(cl.Fore.RED+"-->guess left:", chanceLeft)
        if(chanceLeft == 0):
            print(cl.Fore.RED+"you lost):")
            print(cl.Fore.GREEN+"The Number was: ", rand)
            break;
        if guess == 0:
            break;
    else:
        break
            
print(cl.Fore.WHITE+" ")
