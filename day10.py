#multiplication table calculator
number=int(input("enter the number you want the table for : "))
for i in range(1,11):
    product=number*i
    print(f"{number} x {i} = {product}" )