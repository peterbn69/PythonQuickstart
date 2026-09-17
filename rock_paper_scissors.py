import random

ARTS = {
    0: '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    1: '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
    2: '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
}

NAMES = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}

# Adding a new option later only means updating this dict.
WINS_AGAINST = {0: 2, 1: 0, 2: 1}

def get_user_choice() -> int:
    prompt = ('What is your choice?\n' +
              '\n'.join(f'{num} - {name}' for num, name in NAMES.items()) +
              '\nEnter a number > ')

    while True:
        raw = input(prompt)
        if raw.isdigit() and int(raw) in NAMES: return int(raw)
        print(f'Invalid input. Choose a number between 0 and {len(NAMES) - 1}.\n')

def get_computer_choice() -> int: return random.choice(list(NAMES))

def determine_winner(user_choice: int, computer_choice: int) -> str:
    if user_choice == computer_choice: return 'Draw!'
    if WINS_AGAINST[user_choice] == computer_choice: return 'You won!'
    return 'I won!'

def main() -> None:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f'You chose: {NAMES[user_choice]}{ARTS[user_choice]}')
    print(f'I chose: {NAMES[computer_choice]}{ARTS[computer_choice]}')
    print(determine_winner(user_choice, computer_choice))

if __name__ == '__main__': main()