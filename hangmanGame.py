import time
import random 

def controller():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global word_copy
    word_to_guess = ["plants","january","border","image","film","promise", "kids","lungs","doll","rhyme","damage"]
    word = random.choice(word_to_guess)
    word_copy = word
    length = len(word)
    count = 0

    display = '_' * length
    already_guessed = []
    play_game= ""

#Game playi
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game

    limit = 6
    guess = input("This is the hangman word " + display + ", Enter your guess\n")

    guess = guess.strip()
    if( len(guess.strip()) == 0 or len(guess.strip()) >= 2 or not guess.isalpha()):
        print("Invalid input, please guess an alphabet")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        idxs = []
        
        ##replace both the loops with lambda functions
        for idx, val in enumerate(word):
            if(val == guess):
                idxs.append(idx)

        for index in idxs:
            word = word[0:index] + "_" + word[index+1:]
            display = display[0: index] + guess + display[index+1:]

        idxs.clear()

        print(display+ "\n")

        if len(display) != length:
            hangman()

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        #wrong letter
        count += 1

        if(count == 1):
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

            print("Wrong Guess, " + str(limit - count) + " chances remaining.\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

            print("Wrong Guess, " + str(limit - count) + " chances remaining.\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

            print("Wrong Guess, " + str(limit - count) + " chances remaining.\n")


        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

            print("Wrong Guess, " + str(limit - count) + " chances remaining.\n")


        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |    /\n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

            print("Wrong Guess, " + str(limit - count) + " chances remaining.\n")


        elif count == 6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

            print("Wrong Guess, " + str(limit - count) + " chances remaining.\n")
            print("The word was:", already_guessed, word_copy)
            play_loop()

    if word == "_" * length:
        print("Congrats! You have guesses the word correctly.")
        play_loop()

    elif count != limit:
        hangman()

#To create a menu driven game play again facility
def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = Yes n = No\n")

    #case 1: wrong input
    while play_game not in ["Y", "y", "n", "N"]:
        print("Invalid input\n")
        play_game = input("Do you want to play again? y = Yes n = No\n")

    #case 2: Correct Input
    if play_game in ["Y", "y"]:
        controller()
        hangman()

    elif play_game in ["n" or "N"]:
        print("Thanks for playing! Hope you stop by again")
        exit()

if __name__ == "__main__":
    
    print("This is hangman game")
    name = input("Please enter your name\n")

    print("Hello " + name)
    time.sleep(1)
    print("Welcome to hangman Game.\n")
    time.sleep(2)

    controller()
    hangman()

