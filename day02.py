#love calculator
#taking two names and finding out how many times each letter 
# in the word TRUE LOVE occurs in both the partner's names
def love_calculator(name1,name2):
    combined_names=name1+name2
    lower_names=combined_names.lower()

    t=lower_names.count("t")
    r=lower_names.count("r")
    u=lower_names.count("u")
    e=lower_names.count("e")
    first=t+r+u+e
    l=lower_names.count("l")
    o=lower_names.count("o")
    v=lower_names.count("v")
    e=lower_names.count("e")
    second=l+o+v+e

    score=int(str(first)+str(second))
    
    print(f"love score is {score}")
love_calculator("rahul","leila")
       
	
	
	
