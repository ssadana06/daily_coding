#hangman game
#create a list of the words to be used in the game
import random
import hangman_words
word_list=["apple","mango","kiwi"]
#create placeholders for the words
placeholder=""
#variable to store the chosen word
chosen_word=random.choice(hangman_words.word_list)
#print(chosen_word)
word_length=len(chosen_word)
for position in range(word_length):
	    placeholder+="_"
print(placeholder)
correct_letters=[]
game_over=False
lives=12
while not game_over:
    guess=input("guess a letter ")
    if guess in correct_letters:
      print(f"you have already guessed a {guess}")

    if guess not in chosen_word:
          print(f"guessed letter {guess} not in word , you lost a life")
    display=""
    for letter in chosen_word:
          if letter==guess:
                display+=letter
                correct_letters.append(letter)
          elif letter in correct_letters:
                display+=letter
          
          else:
                display+="_"
    print(display)
    
    
    
    if guess not in chosen_word:
           lives-=1
           print(f"you have {lives} lives left")
           if lives==0:
                  game_over=True
                  print(f"the word was {chosen_word}")
                  print("lives over ,you lose")

    

    if "_" not in display:
           game_over=True
           print("you guessed the word")
    
    
		
		


	





