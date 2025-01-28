import pandas as pd # type: ignore

def moving_average_crossover(data):
    short_window = 10
    long_window = 50

    data['SMA_short'] = data['close'].rolling(window=short_window).mean()
    data['SMA_long'] = data['close'].rolling(window=long_window).mean()

    data['signal'] = (data['SMA_short'] > data['SMA_long']).astype(int)
    data['position'] = data['signal'].diff()
    return data
