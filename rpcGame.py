import time
import random


def play_loop():
    print("Do you want to play again? y - Yes  n - No")

    choice = input()
    if choice not in ["Y", "y", "n", "N"]:
        print("Invalid input, Do you want to play again? y - Yes  n - No")
        play_loop()

    elif choice in ["Y", "y"]:
        rpc_main()
    
    else:
        exit()

def rpc_main():
    bag_of_choice = ["rock", "paper", "scissors"]
    
    user_choice = input("Choose among Rock Paper and Scissor")
    computer_choice = random.choice(bag_of_choice)
    user_choice = user_choice.lower()

    if user_choice not in bag_of_choice:
        print("Invalid input, try again by typing rock, paper or scissors.\n")
    
    else:
        if(user_choice == computer_choice):
            print("It's a draw, you both chose " + user_choice)

        elif user_choice == "paper" and computer_choice == "scissors":
            print("You lose. Scissors cut Paper.")

        elif user_choice == "rock" and computer_choice == "paper":   
            print("You lose. Paper covers Rocks.")
        
        elif user_choice == "scissors" and computer_choice == "paper":
            print("It's a win. Scissors cut Paper.")

        elif user_choice == "paper" and computer_choice == "rock":
            print("It's a win. Paper covers rock")

        elif user_choice == "rock" and computer_choice == "scissors":
            print("It's a win. Rock crushes scissors.")

        elif user_choice == "rock" and computer_choice == "scissors":
            print("You lose. Rock crushes scissors.")
                    
        print("Thanks for playing Rock Paper and Scissors.\n")

    play_loop()

if __name__ == "__main__":
    print("welcome to Rock Paper and Scissor's Game")
    player_name = input("Please enter your name")

    print("Welcome " + player_name)
    print("Let the fun begin in....")
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    
    rpc_main()
