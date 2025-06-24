def number_game():
    num=[10,9,8,7,6,5]
    arr=[]
    while num:
        alice_min=min(num)
        print("minimum element removed by alice")
        num.remove(alice_min)
        print(num)
        bob_min=min(num)
        print("minimum element removed by bob")
        num.remove(bob_min)
        print(num)
        arr.append(alice_min) 
        arr.append(bob_min)
    print("final list : ")
    print(arr)
     
number_game()    