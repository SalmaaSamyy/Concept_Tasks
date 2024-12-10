'''

Problem 3 : "Word Scramble Game"   // search for how to scramble word in python what is the functions We need
Description:
Create a word scramble game where the program randomly scrambles a word and gives the player a set number of attempts to guess the original word.
Requirements:
The program should start by selecting a random word from a predefined list of words.
The selected word should be scrambled (characters shuffled in a random order).
Display the scramble	d word to the player and ask them to guess the original word.
The player should have 5 attempts to guess the word correctly.
For each incorrect guess, the player should be informed how many attempts they have left.
If the player guesses correctly within the attempts, display a congratulatory message.
If the player runs out of attempts, reveal the original word.
Handle invalid input gracefully (e.g., empty input).
Example Interaction:
Example Word:
Suppose the chosen word is "apple", which the program scrambles to "pleap".

Game Flow: 
Welcome to the Word Scramble Game!
Try to guess the original word from the scrambled word: pleap
pYou have 5 attempts.
'''

import random


words = ['sky' , 'school' , 'world' , 'apple']

chosen_word = random.choice(words)


letters = list(chosen_word)  # Convert the word into a list of letters
random.shuffle(letters)  # Shuffle the letters in place
shuffled_word = ''.join(letters)  # Join them back into a string

print (f"Try to guess the orginal word , you have 5 attemps : {shuffled_word} ")

attemps = 5
while attemps > 0:
    guess = input("Enter your geuss : ")
    
    if guess == chosen_word:
        print ("correct guess..!")
        break
    else :
        attemps-=1
        if attemps > 0 :
            print(f"incorrect , try again. you have {attemps} attemps left")
        else:
            print(f"You’re out of attempts! The correct word was {chosen_word}")    




