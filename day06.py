import random
from os import system
start=input("do you want to play a game of blackjack? type 'y' or 'n' ")
system("cls")
numbers=[11,2,3,4,5,6,7,8,9,10,10,10,10]
your_cards=[]
random_nums=random.sample(numbers,k=2)
your_cards.append(random_nums)
current_score=sum(random_nums)
print(f"your cards:{random_nums} , current_score :{current_score}")
computer_card=[]
a=random.choice(numbers)
computer_card.append(a)
print(f"computer's first card : [{computer_card}]")

while True:
        next_move=input("type 'hit' to get another card , type 'stand' to pass : ")
        if  next_move=="hit":
                a=random.choice(numbers)
                your_cards.append(a)
                print(f"your cards:{random_nums} , current_score :{current_score}")
                print(f"computer's first card : [{computer_card}]")
        else:
                print("no")
""""
if sum(your_cards)>sum(computer_card):
        print("you win ")
else:
        print("you lose ")
        """