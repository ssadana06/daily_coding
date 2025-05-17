#reversing a sentence
sentence=input("enter your sentence : ")
split_sentence=sentence.split()
for item in split_sentence:
    print(item[-1::])
