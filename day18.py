def first_unique_char():
    string=input("enter the word : ")
    for item in string:
        if string.count(item)==1:
            print(string.index(item))
            break
        else:
            return -1
first_unique_char()
