#reversing a sentence
sentence=input("enter your sentence : ")
split_sentence=sentence.split()
for item in split_sentence:
    reversed=split_sentence[::-1]
print(reversed)
