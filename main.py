import random
import json
import hangman_art


def load_words(level):
    with open("words.json", "r") as file:
        data = json.load(file)
    return data[level]


def create_display(word):
    return ["_"] * len(word)


def get_input(used_letters):
    while True:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only ONE valid letter.")
        elif guess in used_letters:
            print("You already tried this letter.")
        else:
            return guess


def update_word(word, display, guess):
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess
    return display


def select_level():
    print("Choose difficulty:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")

    choice = input("Your choice: ").strip()

    if choice == "1":
        return "easy"
    elif choice == "2":
        return "medium"
    elif choice == "3":
        return "hard"
    else:
        print("Invalid choice, setting to Medium.")
        return "medium"


def play():
    print(hangman_art.logo)

    level = select_level()
    words = load_words(level)
    word = random.choice(words)

    display = create_display(word)
    used_letters = []
    lives = 6

    print("\nLet's start!")
    print("Word length:", len(word))
    print(" ".join(display))
    print(hangman_art.stages[lives])

    while lives > 0:
        guess = get_input(used_letters)
        used_letters.append(guess)

        if guess in word:
            display = update_word(word, display, guess)
            print(f"Nice! '{guess}' is correct.")
        else:
            lives -= 1
            print(f"Oops! '{guess}' is not in the word.")
            print("Lives left:", lives)
            print(hangman_art.stages[lives])

        print(" ".join(display))
        print("Used letters:", ", ".join(used_letters))

        if "_" not in display:
            print(f"\n You won! The word was '{word}'")

    print(f"\n Game over! The word was '{word}'")


play()