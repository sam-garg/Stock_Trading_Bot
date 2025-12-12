import logging
from binance.client import Client   
from binance.exceptions import BinanceAPIException, BinanceRequestException

# Log file for History 
logging.basicConfig(
    filename='Trading log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#Logic Part

# Connection part
class  BasicBot:
    def __init__(self, api_key, api_secret):
        try:
            self.client = Client(api_key, api_secret, testnet=True) 
            # testnet is demo account value true means to route all request from demo account.
            logging.info('Connected to the network')
            print("Succesfully Connected")
        except Exception as e:
            logging.error(f"Initialization error: {e}")
            print(f"Connection failed: {e}")

#1. placing market order logic
    def place_order(self, symbol, side, order_type, quantity, price=None): 
        """ Places an order on Binance args:
        symbol (str): which coin pair you want TO TRADE
        side (str): buy or sell
        order type (str): market or limit
        quantity (float): how much you wanna buy
        price (float but optional for market): for limit orders only
        """
        try:
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity,
            }
    #added limit for limit orders

            if order_type == 'LIMIT':
                if not price:
                    raise ValueError("Price is required for limit orders.")
                    params['price']=price
                    params['timeInforce']='GTC'  # to tell binance, [GTC] untill cancelled 

            elif order_type == 'STOP':
                if not price or not stop_price:
                    raise ValueError("Stop limit orders require both limit and stop price.")
                    params['price']=price
                    params['stop_price']=stop_price
                    params['timeInforce']='GTC'  # to tell binance [GTC] untill cancelled 
                    #contract price is last price a trade happened ... there are two types of current price 1. mark price calculated average, 2. contract price actual price trade done
                    params['workingtype']='contract_price' 
                
            # api
            logging.info(f"sending order details: {params}")
            response = self.client.futures_create_order(**params)

            logging.info(f"Order placed: {response}")
            return response

        except BinanceAPIException as e:
            logging.error(f"Binance Api error: {e.message}")
            return {"error": {e.message}}

        except Exception as e:
            logging.error(f"General Error: {e}")

    def check_balance(self, specific_coin='USDT'):
        """ Balance checker """
        try:
            info = self.client.futures_account()
            for asset in info['assets']:
                if asses['asset'] == 'USDT':  #USDT is tether coin, change usdt to specific_coins by defualt it is usdt
                    return asset['walletBalance']

        except Exception as e:
            logging.error(f"Error while checking the balance: {e}")
            return None