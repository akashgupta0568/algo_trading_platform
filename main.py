import pandas as pd 
from broker_api import get_historical_data, place_order
from strategies import moving_average_crossover

symbol = 'AAPL'
data = get_historical_data(symbol)

# Convert to DataFrame
df = pd.DataFrame({
    'time': [bar.t for bar in data],
    'close': [bar.c for bar in data]
})

df = moving_average_crossover(df)

if df['position'].iloc[-1] == 1:
    print(f"Buying {symbol}!")
    place_order(symbol, qty=1, side='buy')
elif df['position'].iloc[-1] == -1:
    print(f"Selling {symbol}!")
    place_order(symbol, qty=1, side='sell')
