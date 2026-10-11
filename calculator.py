import os

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def ask_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number.")

def ask_operation() -> str:
    while True:
        op = input("Pick an operation (+, -, *, /): ").strip()
        if op in operations:
            return op
        print("Invalid operation.")

def ask_continue(result: float) -> bool:
    while True:
        choice = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ").strip().lower()
        if choice in ("y", "n"):
            return choice == "y"
        print("Please type 'y' or 'n'.")

def main():
    while True:
        clear()
        result = ask_number("First number: ")
        keep_going = True

        while keep_going:
            op = ask_operation()
            while True:
                number = ask_number("Second number: ")
                if op == "/" and number == 0:
                    print("Cannot divide by zero.")
                    continue
                break

            answer = operations[op](result, number)
            print(f"{result} {op} {number} = {answer}")
            
            result = answer
            keep_going = ask_continue(result)

if __name__ == "__main__":
    main()
