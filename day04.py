from os import system
# silent aunction program 
#the highest biddder wins

#others=input("are there any other bidders ? type 'yes' or 'no'")
bidding_dict={}
def winner_bidder():
        print("welcome to silent aunction\n")
        name=input('what is your name? : ')
        bid=int(input("what is your bid? : $"))
        bidding_dict[name]=bid
        others=input("are there any other bidders ? type 'yes' or 'no'")
        if others=='yes':
            system('cls')
            winner_bidder()
        else:
            system('cls')
            highest_bid=0
            winner=""
            for bidder in bidding_dict:
                bid_amount=bidding_dict[bidder]
                if bid_amount>highest_bid:
                    highest_bid=bid_amount
                    winner=bidder
            print(f"the highest bidder is {winner} with amount{highest_bid}")       
       

        


winner_bidder()   

