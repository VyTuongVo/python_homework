
def make_hangman(the_word):
    guesses = []

    def hangman_closure(words):  # Letters will be added in here and then it will get append to guesses
        guesses.append(words)

        display_word = []
        for letter in the_word:
            if letter in guesses:
                display_word.append(letter)
            else:
                display_word.append("_")
        print(display_word)

        return all(char in guesses for char in secret_word)

    return hangman_closure

        
if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").lower()  

    game = make_hangman(secret_word)

    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter one letter at a time.")
            continue
        result = game(guess)
        if result:
            print("Congratulations! You got the words!")
            break
