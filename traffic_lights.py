from itertools import cycle
import time
import os

os.system("")
RESET = "\033[0m"

def ask_time(color: str) -> int:
    while True:
        try:
            duration = int(input(f"Enter time in seconds for {color} light: "))
            if duration > 0:
                return duration
        except ValueError:
            pass
        print("Time must be a positive integer.")

def main():
    states = {
        "🔴 RED": (ask_time("red"), "STOP!", "\033[91m"),
        "🟢 GREEN": (ask_time("green"), "GO AHEAD!", "\033[92m"),
        "🟡 YELLOW": (3, "SLOW DOWN!", "\033[93m"),
    }

    for color, (seconds, message, ansi) in cycle(states.items()):
        print(f"{ansi}{message}{RESET}")
        for i in range(seconds, 0, -1):
            print(f"{ansi}{color} - {i}{RESET}")
            time.sleep(1)
        print()

if __name__ == "__main__":
    main()