import random
import hangman_art
import hangman_words

stage = hangman_art.stages
word_list = hangman_words.word_list
print(hangman_art.logo)
n = len(word_list) - 1
chosen_word = word_list[random.randint(0, n)]
n_guess = len(stage)
length = len(chosen_word)
answer = []
guesses = []
for j in range(0, length):
    answer.append("_")
flag = 1
while flag:
    guess = input("Enter your guess ").lower()
    if guess in guesses:
        print(f"You've already chosen {guess},try again")
    else:
        guesses.append(guess)

        if guess in chosen_word:
            for i in range(0, len(chosen_word)):
                if chosen_word[i] == guess:
                    length -= 1
                    answer[i] = guess
            print(" ".join(answer))
        else:
            print(stage[n_guess - 1])
            print(" ".join(answer))
            print("Wrong Guess !!")
            n_guess -= 1
        if n_guess == 0:
            print("Game over !!")
            print(f"The correct word was {chosen_word}")
            flag = 0
        elif length == 0:
            print("You guessed the right word !")
            flag = 0
