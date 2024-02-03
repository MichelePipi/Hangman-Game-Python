# Set constants
MAX_GUESSES = 7

# Choose a random word
word = "phone"

# Get the length of the word
word_length = len(word)

# Set list for correct guesses
player_guesses = ["_" for _ in range(word_length)]

# Set initial guess count
guesses_left = MAX_GUESSES

# Set loop case
finished = False

# Print length of word
print(f"The word has {word_length} letters")

# Loop
while not finished:
    # Check if the player has run out of guesses
    if guesses_left < 1:
        print("Oh no! Looks like you've ran out of guesses. GAME OVER")
        finished = True
        continue
    # Convert guess list into string and check if it matches the secret word (they won!)
    if "".join(player_guesses) == word:
        print("You've won! Congratulations!")
        finished = True
        continue
    # Show the player how many letters are missing
    print("The word is ", end="")
    print(*player_guesses)
    print(f"You have {guesses_left} guess(es) left.")
    # Ask user to input guess
    guess = input("Enter guess: ")
    # If the guess is anywhere in the word
    if guess in word:
        print("Nice one! Your guess was in the word!")
        # Find each spot in the word the guess is
        for i, letter in enumerate(word):
            # Found a spot where the letter is
            if guess == letter:
                # Reveal the location
                player_guesses[i] = guess
    else:  # If it isn't decrease how many guesses they have left
        print("Noo! Wrong guess!")
        guesses_left = guesses_left - 1
