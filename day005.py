from os import system

def python_calculator():
    def add(first_num,next_num):
     
     return first_num+next_num
     
    def subtract(first_num,next_num):
        return first_num-next_num
    
    def multiply(first_num,next_num):
        return first_num*next_num
    
    def divide(first_num,next_num):
        return first_num/next_num
    
    calculate={
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide
    }
    first_num=float(input("what is the first number ?: "))
    for operator in calculate:
        print(operator)
    operation=input("pick an operation : ")
    next_num=float(input("whats the next number : "))

    result=float(calculate[operation](first_num,next_num))
    print(f"{first_num} {operation}  {next_num} = {result}")

   
    should_continue=True
    while should_continue:      
        go_on=input(f"type 'yes' if u want to continue with {result}  or  type 'no' if you want to start again : ")
        if go_on=="yes":
            num=float(input("what is the next number : "))
            for operator in calculate:
                print(operator)
            operation=input("pick an operation : ")
            previous=result
            answer = calculate[operation](result, num)
            result = answer
            print(f"{previous} {operation} {num} = {answer}")
        else:
            should_continue = False
            system("cls")
            python_calculator() 
                    
        
        
       
python_calculator()      
        


