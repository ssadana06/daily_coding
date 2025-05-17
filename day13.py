#prime number checker
def is_prime():
    num=int(input("enter a number to check if it is prime or not : "))
    for item in range(2,num):
        if num%item==0:
            print("False")
            break
    else:
        print("True") 
            
is_prime()