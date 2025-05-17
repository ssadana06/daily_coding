#passsword checker 
alphabets=[
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers=["1","2","3","4","5","6","7","8","9","0"]
special_characters=["!","@","#","$","%","^","&","*","+","_","-"]

is_running=True
while is_running:
    password=input("enter a password : ")
    has_alphabets= any(char.isalpha() for char in password)  
    
    has_digits=any(char.isdigit() for char in password)
        
    special_char= any(char in special_characters for char in password)
    score=has_alphabets+has_digits+special_char
    if score==1:
        print(" password is weak, generate another password")
    elif score==2:
        print("password is moderately strong , generate a strong password")
        
    else:
        print("password is strong, you can proceed")
        is_running=False
    

