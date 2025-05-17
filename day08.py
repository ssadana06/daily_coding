#number guessing game 
import random
from os import system
def guessing_number_game(): 
    re_game="yes"
    
    while re_game=="yes":
         random_num=random.randrange(1,100)
         number=0
    
         while number!=random_num:
            
            number=int(input("enter a number : "))
            
            if number>random_num:
                print("your guess is too high")
            elif number<random_num:
                print("your guess is too low")
            else:
                print("you guessed the number")
            

guessing_number_game()    


