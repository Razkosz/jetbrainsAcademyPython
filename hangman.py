import random

words_source = ("python", "java", "swift", "javascript")
wins = 0
loses = 0
english_alphabet = set("qwertyuiopasdfghjklzxcvbnm")

def hangman(word_library):
    global wins
    global loses
    word_str = random.choice(word_library)
    word = list(word_str)
    word_letters = frozenset(word)
    guessed_letters = set()
    coded_word = ['-'] * len(word)
    attempts = 8
    guess = ""
    while attempts > 0:
        check = False
        while not check:
            print("".join(coded_word))
            guess = input("Input a letter:")
            check = check_correctness_of_input(guess)
        if guess in word_letters and guess not in guessed_letters:
            for index, letter in enumerate(word):
                if letter == guess:
                    coded_word[index] = guess
        else:
            if guess not in guessed_letters:
                print("That letter doesn't appear in the word.")
                attempts -= 1
            else:
                print("You've already guessed this letter.")
        guessed_letters.add(guess)
        print('')
        if '-' not in coded_word:
            break
    else:
        print("You lost!")
        loses += 1
    if attempts > 0:
        print(f"You guessed the word {word_str}!")
        print("You survived!")
        wins += 1


def check_correctness_of_input(char):
    if len(char) != 1:
        print("Please, input a single letter.")
        return False
    if char not in english_alphabet:
        print("Please, enter a lowercase letter from the English alphabet.")
        return False
    return True


def menu():
    option = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if option == "play":
        print("")
        hangman(words_source)
        menu()
    elif option == "results":
        print(f"You won: {wins} times.")
        print(f"You lost: {loses} times.")
        menu()
    elif option == "exit":
        pass
    else:
        menu()


if __name__ == "__main__":
    print("H A N G M A N")
    menu()
