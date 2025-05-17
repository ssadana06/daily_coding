# ask the user to enter 3 numbers and find the maximun number
num1=int((input("enter number 1 : ")))
num2=int((input("enter number 2: ")))
num3=int((input("enter number 3 : ")))
if num1>num2 and num1>num3:
    print(f"the largest number is : {num1} ")
elif num2>num1 and num2>num3:
    print(f"the largest number is : {num2}")
else:
    print(f"the largest number is : {num3}")


