# Python Practice Projects

A collection of small command-line programs I wrote while learning Python.
Each script is self-contained: no setup, no dependencies, and no script imports another one.

## Projects

| Script | What it does | Concepts practiced |
|---|---|---|
| [`blind_auction.py`](blind_auction.py) | Collects bids from several people, clears the screen between bidders, and announces the winner. A repeat bidder keeps their highest bid. | Dictionaries, `max()` with a `key`, input validation |
| [`caesar_cipher.py`](caesar_cipher.py) | Encodes or decodes a message with a Caesar cipher. Letters are shifted (any integer shift works) and other characters remain unchanged. | `str.maketrans`, modulo arithmetic, string constants |
| [`calculator.py`](calculator.py) | Calculator that chains operations (`+ - * /`): continue with the previous result or start a new calculation. Rejects invalid input and division by zero. | Dictionary of lambdas, functions, nested loops, validation |
| [`hangman.py`](hangman.py) | Classic hangman with ASCII art. Guess a random word one letter at a time with 6 lives. | Sets, tuples, `while` loops, string handling |
| [`password_generator.py`](password_generator.py) | Generates a random password with the number of letters, symbols and digits chosen by users. | `secrets` module, list comprehensions, shuffling |
| [`rock_paper_scissors.py`](rock_paper_scissors.py) | One round of rock-paper-scissors against the computer, with ASCII art. | Dictionaries as lookup tables, `random` |
| [`traffic_lights.py`](traffic_lights.py) | Traffic light simulator with a countdown. Red and green durations are set by users (yellow is fixed at 3 seconds). | `itertools.cycle`, tuple unpacking, ANSI colors, `time.sleep` |

## Requirements

- Python 3.8 or newer (developed on Python 3.14)
- Standard library only, nothing to install

## How to run

Open a terminal in the project folder and run any script with Python:

```bash
python hangman.py
```

On macOS and Linux you may need `python3` instead of `python`.

## Notes

- `calculator.py` and `traffic_lights.py` run until you stop them. Press `Ctrl+C` to exit.
- `blind_auction.py` and `calculator.py` clear the screen using `cls` (Windows) or `clear` (macOS/Linux), so run them from a real terminal.
- `traffic_lights.py` uses emojis and ANSI colors. Use a modern terminal such as Windows Terminal, macOS Terminal or any common Linux terminal; very old consoles may show garbled characters.
- The scripts are flat in one folder on purpose. They are small and independent, so extra folders would add structure without adding clarity.

## License

Released under the [MIT License](LICENSE).
