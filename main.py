import random
from words import word_list

# Hangman çizimlerini içeren liste
def display_hangman(wrong):
    hangman_pics = [
        """
         ------
        |    |
        |      
        |     
        |
       _|_
        """,
        """
         ------
        |    |
        |    O  
        |     
        |
       _|_
        """,
        """
         ------
        |    |
        |    O  
        |    |
        |
       _|_
        """,
        """
         ------
        |    |
        |    O  
        |   /| 
        |
       _|_
        """,
        """
         ------
        |    |
        |    O  
        |   /|\\ 
        |
       _|_
        """,
        """
         ------
        |    |
        |    O  
        |   /|\\  
        |   / 
       _|_
        """,
        """
         ------
        |    |
        |    O  
        |   /|\\  
        |   / \\
       _|_
        """
    ]
    
    print(hangman_pics[wrong])

# Seçilen kelimenin durumunu görüntüleyen fonksiyon
def print_word(selected_word, guessed_letters):
    for char in selected_word:
        if char.upper() in guessed_letters:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()

# Hangman oyununun ana döngüsünü içeren fonksiyon
def play_hangman():
    print("Let's play hangman!")

    selected_word = random.choice(word_list)

    guessed_letters = []
    wrong_letters = []

    word_length = len(selected_word)
    wrong_guess_count = 0
    correct_letters_count = 0

    while wrong_guess_count < 6 and correct_letters_count < word_length:
        print("\nLetters guessed so far: ", [letter for letter in guessed_letters + wrong_letters if letter not in selected_word.upper()])
        
        display_hangman(wrong_guess_count)
        print_word(selected_word, guessed_letters)
        
        guess = input("\nEnter a letter or word guess: ").upper()
        
        if len(guess) == 1:  # Kullanıcının girdiği tahmin 1 karakter ise harf tahmini olarak kabul ediyoruz
            if guess in guessed_letters or guess in wrong_letters:
                print("You already guessed that letter.")
            else:
                if guess in selected_word.upper():
                    guessed_letters.append(guess)
                    correct_letters_count += selected_word.upper().count(guess)
                else:
                    wrong_guess_count += 1
                    wrong_letters.append(guess)
        else:  # Kullanıcının girdiği tahmin 1 karakterden uzun ise kelime tahmini olarak kabul ediyoruz
            if guess == selected_word.upper():
                print("\nCongrats! You guessed the word:", selected_word)
                print("You Win :)")
                break
            else:
                print("Sorry, your guess is incorrect.")
                wrong_guess_count += 1

    if wrong_guess_count == 6:
        display_hangman(wrong_guess_count)
        print("\nSorry, you lost! The word was:", selected_word)

play_hangman()

play_again = input("\nDo you want to play again? (Y/N): ").upper()
if play_again == "Y":
    play_hangman()



