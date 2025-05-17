#word frequency counter
sentence=input("enter your sentence : ")
split_words=sentence.split()
word_freq={}
for word in split_words :
    if word in word_freq:
        word_freq[word]+=1
    else:
        word_freq[word]=1
for word , freq in word_freq.items():
    print({f"{word},{freq}"})

    

