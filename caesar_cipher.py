from string import ascii_lowercase as alphabet
from string import ascii_uppercase as ALPHABET

def shift_text(text: str, shift: int) -> str:
    k = shift % 26
    table = str.maketrans(alphabet + ALPHABET, alphabet[k:] + alphabet[:k] + ALPHABET[k:] + ALPHABET[:k])
    return text.translate(table)

def run_cipher(mode: str) -> None:
    msg = input("Message: ")
    while True:
        try:
            shift = int(input("Shift: "))
            break
        except ValueError:
            print("Invalid shift. Please enter a valid integer.")
    if mode == "decode":
        shift = -shift
    print(f"{mode.capitalize()}d message: {shift_text(msg, shift)}\n")

def main() -> None:
    print("Welcome to Caesar Cipher!")
    while True:
        print("Type 'encode' to encode a message or 'decode' to decode it. Type 'exit' to quit.")
        mode = input("Mode: ").lower()
        if mode in ("encode", "decode"):
            run_cipher(mode)
        elif mode == "exit":
            print("Thank you for using Caesar Cipher!")
            break
        else:
            print("Invalid mode. Please try again.\n")

if __name__ == "__main__":
    main()