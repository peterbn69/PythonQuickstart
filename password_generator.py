import secrets
import string

LETTERS = string.ascii_letters
NUMBERS = string.digits
SYMBOLS = '!#$%&()*+@'

def ask_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0: return value
            print('Please enter a non-negative integer.')
        except ValueError: print('Please enter a valid integer.')

def generate_password(n_letters, n_symbols, n_numbers):
    chars = (
        [secrets.choice(LETTERS) for _ in range(n_letters)] +
        [secrets.choice(SYMBOLS) for _ in range(n_symbols)] +
        [secrets.choice(NUMBERS) for _ in range(n_numbers)]
    )
    secrets.SystemRandom().shuffle(chars)
    return ''.join(chars)

def main():
    print('Welcome to the PyPassword Generator!')
    n_letters = ask_int('How many letters would you like in your password? ')
    n_symbols = ask_int('How many symbols would you like in your password? ')
    n_numbers = ask_int('How many numbers would you like in your password? ')

    if n_letters + n_symbols + n_numbers == 0:
        print('Your password cannot be empty.')
        return

    print(f'Your password is: {generate_password(n_letters, n_symbols, n_numbers)}')

if __name__ == '__main__': main()