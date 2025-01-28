import alpaca_trade_api as tradeapi 
from config import API_KEY, API_SECRET, BASE_URL

# Connect to Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, base_url=BASE_URL)

def get_account():
    account = api.get_account()
    return account

def place_order(symbol, qty, side):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type='market',
        time_in_force='gtc'
    )

def get_historical_data(symbol, timeframe='minute', limit=100):
    barset = api.get_barset(symbol, timeframe, limit=limit)
    return barset[symbol]
