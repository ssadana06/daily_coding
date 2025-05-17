#even odd counter 
nums=input("enter the numbers you wish to check")
numbers=list(map(int,nums.split()))
even=[]
odd=[]
for item in numbers:
    if item%2==0:
        even.append(item)
        a=len(even)
        
    else:
        odd.append(item)
        b=len(odd)
print(f"even numbers : {a}")   
print(f"odd numbers : {b}")    
