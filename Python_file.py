#############################################################################
##                                                                         ##
##                        Mini Programming Projects                        ##
##                          Ngonidzashe Mandiveyi                          ##
##                               Fall 2020                                 ##
##                                                                         ##
#############################################################################

## This is is a program that generates a random number between 0 and n

import random
user_input = input("Roll the dice?")
n = int(input("Number of sides?"))

def roll_dice(user_input, n):
    if user_input == "yes":
        print(random.randrange(1,n,1))
    else:
        exit

roll_dice(user_input, n);

def factorial(n):
    result = 1
    for num in range(1, n+1):
        result *= num

    return result

    
