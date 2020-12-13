import random
from hangman_words import word_list
from hangman_art import logo
print(logo)
from hangman_art import stages

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Create a variable called 'lives' to keep track of the number of lives left. 
lives=6


display = []
for i in chosen_word:
  display.append("_")
print(display)

while end_of_game==False:
  #Check guessed letter
  while lives>0:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
      for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
          display[i]=guess
    else:
      lives-=1
      print(stages[lives])
    
    if "_" not in display:
      end_of_game=True
      print("You win!")
      break
  if "_" in display and lives==0:
    print("You Lose!")
    end_of_game=True
    break

print(display)
print("The correct word is " + chosen_word)        