
def hang_man(word):
    word = "python"
    num_tries = len(word)
    print(f"tries left: {num_tries}")
    print("-" * 8)
    print("|      |")
    for num in range(4):
        print("|")
    print("_")


    num_of_tries = len(word)
    i = 0
    ready_to_play = input("Are you ready to play hangman? (yes/no): ")
    if ready_to_play.lower() == "no":
        print("To bad, you're playing anyway!")
    elif ready_to_play.lower() == "yes":
        print("Let's play hangman!!!")
    else:
        print("Invalid input. Starting the game.")

    while i < num_of_tries:
        user_input = input("Enter a letter: ")
        if user_input == word[i]:
            print("Good guess!")
        else:
             print("-" * 8)
             print("|      |")
             print("|      O")
             for num in range(4):
                print("|")
        print("_")
        num_tries -= 1
        print(f" Tries left: {num_tries}")
        i += 1
    
    print("You lost!")  # Add a message for when the maximum attempts are exhausted

hang_man("word")

#........................................................
#some Ideas to think about: instead of setting the max amount of tries to the length of the word. lets give the user a max of 7 incorrect guesses. 
# therefore the user can continue guessing until they get the right word or phrase
# if the user enters a number instead of a letter, it says "invalid entry, try again"


# we will be using the replace method to repace the ______ to letters each time the user makes a good guess (hint: the quiz exercice)
"""
# while the number of attempts is equal to the len of the conditional word


   num_of_tries = len(word)
    i = 0
    while  i < num_of_tries:
# ask the user the guess the letter
     user_input = input("Enter a letter: ")
# set a condition 
    if user_input == word[i]:
        print("Good guess!")
    else:
        print("O")
"""