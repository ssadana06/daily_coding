#checking pangram
def pangram():
    alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
    sentence=input("enter your sentence : ")
    sentence=sentence.lower()

    for item in alphabets:
        if item not in sentence:
            return False
    return True   
  
print(pangram())