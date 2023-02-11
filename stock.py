import requests
import json
import winsound
import time
import datetime
import matplotlib.pyplot as plt

def get_data(symbol):
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + symbol + "&apikey=XX"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["Global Quote"]["05. price"]

def calculate_moving_average(prices, window_size):
    weights = [1/window_size for i in range(window_size)]
    moving_average = []
    for i in range(len(prices) - window_size):
        window = prices[i:i+window_size]
        moving_average.append(sum(x*y for x,y in zip(weights, window))
    return moving_average

def is_it_time_to_buy_or_sell(price, moving_average, threshold):
    if (price - moving_average) > threshold:
        return "buy"
    elif (moving_average - price) > threshold:
        return "sell"
    else:
        return "hold"

def play_sound(buy_or_sell):
    if buy_or_sell == "buy":
        winsound.PlaySound("buy.wav", winsound.SND_FILENAME)
    elif buy_or_sell == "sell":
        winsound.PlaySound("sell.wav", winsound.SND_FILENAME)

def main():
    symbols = ["AAPL", "MSFT", "AMZN", "GOOG", "TSLA"]
    window_size = 10
    threshold = 10
    while True:
        prices = []
        for symbol in symbols:
            price = float(get_data(symbol))
            prices.append(price)
            print(f"{symbol}: {price}")
        moving_average = calculate_moving_average(prices, window_size)
        buy_or_sell = is_it_time_to_buy_or_sell(price, moving_average, threshold)
        play_sound(buy_or_sell)
        time.sleep(60)

if __name__ == "__main__":
    main()
