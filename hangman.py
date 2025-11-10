import random

# Step 1: Word list
words = ["python", "computer", "hangman", "program", "developer"]

# Step 2: Randomly choose one word
word = random.choice(words)
word_letters = list(word)

# Step 3: Game variables
guessed_letters = []
display_word = ["_"] * len(word)
attempts = 6

# Step 4: ASCII Hangman Stages
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

# Step 5: Game start
print("🎯 Welcome to Hangman!")
print("You have 6 chances to guess the word.")

# Step 6: Main Game Loop
while attempts > 0 and "_" in display_word:
    print(HANGMAN_PICS[6 - attempts])
    print("\nWord:", " ".join(display_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Remaining attempts: {attempts}")

    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_letters:
        print("✅ Correct! That letter is in the word.")
        for i in range(len(word_letters)):
            if word_letters[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1

# Step 7: Game Over
print(HANGMAN_PICS[6 - attempts])  # Final hangman stage
if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
