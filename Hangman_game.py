import random

def hangman():
    words = ["python", "hangman", "programming", "developer", "challenge"]
    word_to_guess = random.choice(words)
    guessed_letters = set()
    attempts = 6
    word_display = ["_"] * len(word_to_guess)

    print("Welcome to Hangman!")
    print("You have to guess the word. You have 6 incorrect attempts before you lose.")

    while attempts > 0 and "_" in word_display:
        print("\nCurrent word: " + " ".join(word_display))
        print(f"Attempts remaining: {attempts}")
        print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    word_display[index] = guess
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. You lose an attempt.")

    if "_" not in word_display:
        print(f"Congratulations! You've guessed the word: {word_to_guess}")
    else:
        print(f"Game over! The word was: {word_to_guess}")

if __name__ == "__main__":
      hangman()

