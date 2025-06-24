#add digits
#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
while True:
    
    num=int(input("enter a number : "))
   
    remainder=num%10
    qoutient=num//10
    sum_num=remainder+qoutient

    
    if len(str(num))==2:
        remainder_2=sum_num%10
        qoutient_2=sum_num//10
        add_num=remainder_2+qoutient_2
        print(add_num)
    else:
        print(sum_num)
        break

