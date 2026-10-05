import random

WORDS = ("formidable", "example", "hangman", "warrior", "python", "zebra")
STAGES = (
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
)

def main() -> None:
    chosen_word = random.choice(WORDS)
    remaining = set(chosen_word)
    guessed = set()
    lives = 6

    while lives > 0 and remaining:
        print(f"Lives remaining: {lives}")
        print(STAGES[lives])
        print("".join(c if c in guessed else "_" for c in chosen_word))
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha() or guess in guessed:
            print("Invalid or repeated guess. Try again.\n")
            continue
        guessed.add(guess)
        remaining.discard(guess)
        if guess not in chosen_word:
            lives -= 1
        print()

    if lives == 0:
        print(STAGES[0])
        print(f"Game over! The word was '{chosen_word}'")
    else:
        print(f"Congratulations! You guessed the word: {chosen_word}")

if __name__ == "__main__":
    main()