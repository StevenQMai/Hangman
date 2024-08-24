import random
from words import word_list

def get_word():
    word = random.choice(word_list) #takes a random word from the wordlist
    return word.upper() #returns the word as uppercase

def play(word):
    word_completion = "_" * len(word) #initializes the word_completion variables as a string composed of underscores repeated a number of times equal to the length of the "word" string
                                      #also represents the current state of the word being guessed in the hangman game
    guessed = False #initializes value of the guessed variable to be false
    guessed_letters = [] #initializes an empty list that stores all individual guessed letters so far in the game
    guessed_words = [] #initializes an empty list that stores complete words
    tries = 6 #1 try per body part
    print("Lets play Hangman!")
    print(display_hangman(tries)) #displays a varying image from display_hangman() based on how many tries are remaining
    print(word_completion) #prints the desired amount of underscores matching the word length
    print("\n")
    while not guessed and tries > 0: #as long as the word hasn't been guessed yet and the player still has tries remaining:
        guess = input("Please guess a letter or word: ").upper() #takes an input and returns it as uppercase
        if len(guess) == 1 and guess.isalpha(): #if the guess is a letter and the guess is part of the alphabet
            if guess in guessed_letters: #if the guessed letter contains a letter that was already guessed
                print("You already guessed the letter", guess)
            elif guess not in word: #if the guessed letter is not part of the mystery word
                print(guess, "is not in the word.")
                tries -= 1 #substracts a try
                guessed_letters.append(guess) #adds the variable 'guess' to the list of guessed_letters
            else: #if the letter guessed is in the word:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess) #adds this correct guessed letter to the list of guessed_letters
                word_as_list = list(word_completion) #converts the word_completion string into a list and then assigns it to the variable word_as_list
                                                     #afterwards, the word_as_list variable will contain each letter of word_completion as a separate element in a list
                indices = [i for i, letter in enumerate(word) if letter == guess]
                #'enumerate(word)' iterates over characters of the 'word' string and returns pairs of indices and characters
                    #ex: if 'word' = "hello":
                        #enumerate(word) = "(0,'h'), (1,'e'), (2, 'l'), (3, 'l'), (4, 'o')"
                #'for i, letter in enumerate(word)' iterates over each pair returned by 'enumerate(word)'.
                    #'i' represents the index of the character in 'word' and 'letter' represents the character itself
                #'if letter == guess' checks if the current character 'letter' is equal to the guessed letter 'guess'

                #indices = [i for i, letter in enumerate(word) if letter == guess]
                    #constructs a list of indices 'i' where the condition 'letter = guess' is true. In other words, it collects the indices of occurrences of the guessed letter within the word

                #Example: 
                    #if 'word' is "poop" and 'guess' is "p", the list comprehension would produce the list '[0,3]' because "p" appears at indices 0 and 3 within "poop"
                for index in indices: #iterates over each index in the 'indices' list
                                      #these indices represent the positions in the word where the guessed letter 'guess' occurs
                    word_as_list[index] = guess #for each index in 'indices', this line updates the corresponding position in the 'word_as_list' with the guessed letter 'guess'.
                                                #this reveals the correctly guessed letter in the partially completed word
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else: 
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was" + word + ". Maybe next time!" )


def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()