#max number of words found in a sentence
sentence=input("enter the sentence : ").strip()
split_sentence=sentence.split(',')
print(split_sentence)
max_count=0
for item in split_sentence:
       word_count=len(item.split())
       if word_count>max_count:
            max_count=word_count
print(max_count)