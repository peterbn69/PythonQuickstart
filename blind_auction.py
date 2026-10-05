import os

def ask_price() -> float:
    while True:
        try:
            price = float(input("Price: $"))
            if price > 0:
                return price
        except ValueError:
            pass
        print("Enter a positive number.")

def main() -> None:
    bids = {}
    while True:
        name = input("Name: ").strip()
        bids[name] = max(ask_price(), bids.get(name, 0))  # keep a bidder's highest bid

        if input("Type 'yes' if there are more bidders, type otherwise to exit: ").strip().lower() != "yes":
            break
        os.system("cls" if os.name == "nt" else "clear")

    winner, price = max(bids.items(), key=lambda kv: kv[1])
    print(f"The winner is {winner} with a bid of ${price:.2f}.")

if __name__ == "__main__":
    main()