from game_data import data
import random
A,B=random.sample(data,2)
print(f"Compare A : {A['name']} - {A['description']} from {A['country']}")
print(f"Against B : {B['name']} -  {B['description']} from {B['country']}")
#user_ans=input("Who has more followers ? Type A or B ").lower()
current_score=0
correct=True
while correct:
    
    user_ans=input("Who has more followers ? Type A or B ").lower()
    if user_ans=='a' and A['follower_count'] > B['follower_count']:
        current_score+=1
        print(f"you're right ! , current_score :  {current_score}")
        A=A
        B=random.choice(data)
        print(f"Compare A: {A['name']} - {A['description']} from {A['country']}")
        print(f"Against B: {B['name']} - {B['description']} from {B['country']}")

    elif user_ans=='b' and B['follower_count'] > A['follower_count']:
        current_score+=1
        print(f"you're right ! , current_score :  {current_score}")
        A=B
        B=random.choice(data)
        print(f"Compare A: {A['name']} - {A['description']} from {A['country']}")
        print(f"Against B: {B['name']} - {B['description']} from {B['country']}")

    else:
        print(f"sorry that's wrong , final score : {current_score}")
        correct=False
