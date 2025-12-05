import random

# Holds all slots and provides spin functionality
class RouletteWheel:
    def __init__(self):
        self.slots = ["0", "00", "1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34","36"]
        self.red_numbers = {"1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34","36"}
        self.black_numbers = {"2","4","6","8","10","11","13","15","17","20","22","24","26","28","29","31","33","35"}

    def spin(self):
        return random.choice(self.slots)

# Player details and balance
class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Player: {self.name}, Balance: ${self.balance}"

    def place_bet(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def add_winnings(self, amount):
        self.balance += amount

# Controls game flow and logic
class RouletteGame:
    def __init__(self, player):
        self.player = player
        self.wheel = RouletteWheel()

    def calculate_payout(self, bet_type, bet_amount):
        payouts = {"straight": 35, "split": 17, "street": 11, "corner": 8, "line": 5, "dozen": 2, "column": 2, "even money": 1}  # red/black, odd/even, high/low
        return bet_amount * payouts.get(bet_type, 0) + bet_amount

    def play_roulette(self):
        


        print("Welcome to American Roulette!")
        print(self.player)

        # Continue until player quits or runs out of money
        while self.player.balance > 0:
            print(f"Current Balance: ${self.player.balance}")
            bets = []

            # Collect multiple bets
            while True:
                bet_amount = int(input("Enter your bet amount: "))
                if not self.player.place_bet(bet_amount):
                    print("Insufficient balance. Try again.")
                    continue

                print("Choose bet type: straight, dozen, split, street, corner, line, dozen, column, red/black, odd/even, high/low")
                bet_type = input("Enter bet type: ").lower()

                bet_details = []
                if bet_type == "straight":
                    bet_details.append(input("Enter a single number (0, 00, or 1-36): "))
                elif bet_type == "split":
                    bet_details = input("Enter two numbers separated by space: ").split()
                elif bet_type == "street":
                    bet_details = input("Enter three numbers in a row separated by space: ").split()
                elif bet_type == "corner":
                    bet_details = input("Enter four numbers forming a square separated by space: ").split()
                elif bet_type == "line":
                    bet_details = input("Enter six numbers forming two rows separated by space: ").split()
                elif bet_type == "dozen":
                    bet_details.append(input("Enter dozen (1-12, 13-24, 25-36): "))
                elif bet_type == "column":
                    bet_details.append(input("Enter column (1, 2, or 3): "))
                elif bet_type in ["red/black", "odd/even", "high/low"]:
                    bet_details.append(input("Enter choice (red/black, odd/even, high/low): "))

                bets.append({"type": bet_type, "amount": bet_amount, "details": bet_details})

                more_bets = input("Do you want to add another bet? (yes/no): ").lower()
                if more_bets != "yes":
                    break

            # Spin the wheel once for all bets
            result = self.wheel.spin()
            print(f"The wheel landed on: {result}")

            # Process all bets
            for bet in bets:
                win = 0
                bet_type = bet["type"]
                bet_details = bet["details"]
                bet_amount = bet["amount"]

                if bet_type == "straight" and result in bet_details:
                    win = 1
                elif bet_type in ["split", "street", "corner", "line"] and result in bet_details:
                    win = 1
                elif bet_type == "dozen":
                    if result.isdigit():
                        num = int(result)
                        if (bet_details[0] == "1-12" and 1 <= num <= 12) or (bet_details[0] == "13-24" and 13 <= num <= 24) or (bet_details[0] == "25-36" and 25 <= num <= 36):
                            win = 1
                elif bet_type == "column":
                    if result.isdigit():
                        num = int(result)
                        col = (num - 1) % 3 + 1
                        if str(col) == bet_details[0]:
                            win = 1
                elif bet_type == "red/black":
                    if result in self.wheel.red_numbers and bet_details[0] == "red":
                        win = 1
                    elif result in self.wheel.black_numbers and bet_details[0] == "black":
                        win = 1
                elif bet_type == "odd/even":
                    if result.isdigit():
                        num = int(result)
                        if (num % 2 == 0 and bet_details[0] == "even") or (num % 2 == 1 and bet_details[0] == "odd"):
                            win = 1
                elif bet_type == "high/low":
                    if result.isdigit():
                        num = int(result)
                        if (1 <= num <= 18 and bet_details[0] == "low") or (19 <= num <= 36 and bet_details[0] == "high"):
                            win = 1

                if win:
                    winnings = self.calculate_payout(bet_type if bet_type not in ["red/black","odd/even","high/low"] else "even money", bet_amount)
                    self.player.add_winnings(winnings)
                    print(f"Bet on {bet_type} {bet_details} wins! Winnings: ${winnings}")
                else:
                    print(f"Bet on {bet_type} {bet_details} loses.")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break

        print("Game over!")
        print(self.player)

# Start the game
'''
name = input("Enter your name: ")
balance = int(input("Enter your starting balance: "))
player = Player(name, balance)
roulette_game = RouletteGame(player)
roulette_game.play_roulette()
'''