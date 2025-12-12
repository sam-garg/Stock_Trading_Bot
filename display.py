from logic import BasicBot 
from dotenv import load_dotenv
import os

# loading keys
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

def print_menu():
    print("\nWelcome to the stock track bot")
    print("1. Place Market Order")
    print("2. Place Limit Order")
    print("3. Place Stop-Limit Order")
    print("4. Check Balance in Wallet")
    print("5. Exit")
    print("--------------------------------")

# adding a function for checking the input as float
def float_input(x):
    while True:
        try:
            value = float(input(x))
            if value <= 0:
                print("value must be positive")
                continue
            return value
        except ValueError:
            print("Invalid input")

def main():
    bot = BasicBot(API_KEY, API_SECRET)

    while True:
        print_menu()
        choice = input("Select any option from (1-5): ")

        if choice == '5':
            print("Exiting........ Good Bye!")
            break

        if choice == '4':
            bal = bot.check_balance()
            print(f"Current balance: {bal}")
            continue

        if choice in ['1', '2', '3']:
            symbol = input("enter symbol (eg. BTCUSDT for bitcoin USDT): ").upper()
            side = input("enter side BUY or SELL: ").upper()

            if side not in ['BUY', 'SELL']:
                print("Enter a valid side. either BUY or SELL: ")
                continue

            quantity = float_input(f"Enter how much quantity for {symbol}: ")
            result ={}

            if choice == '1': # for market order
                print(f"placing market {side} order for {symbol} {quantity}.")
                result = bot.place_order(symbol,side, 'MARKET', quantity)

            elif choice == '2': # for limit order
                price = float_input("Enter the limit price: ")
                print(f"Placing an Limit {side} order for {symbol} {quantity} at {price}")
                result = bot.place_order(symbol, side, 'LIMIT', quantity, price)

            elif choice == '3': # for stop-limit
                stop = float_input("Enter the price for stop trigger: ")
                limit = float_input("Enter the price for limit trigger: ")
                print(f"Placing STOP-LIMIT {side} order.")
                print(f" Stop Trigger at: {stop} and Limit Trigger at: {limit}")

                #lastly storing the result
                result = bot.place_order(
                    symbol,
                    side,
                    'STOP',
                    quantity,
                    price=limit,
                    stop=stop
                )

        #output
        if "error" in result:
            print(f"Faild to execute order.... {result['error']}")
        else:
            print("\n Order Placed")
            #binance provide few features 
            print(f"   Order ID: {result.get('orderId')}") 
            print(f"   Status: {result.get('status')}")
            print(f"   Summary: {side} {quantity} {symbol}")

if __name__ =="__main__":
    main()
