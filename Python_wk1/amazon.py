table_data = [
    ["Ticker", "Open", "Close"],
    ["AAPL", 363.25, 363.4],
    ["AMZN", 2756.0, 2757.99],
    ["GOOG", 1409.1, 1408.2]
]

amazon_data = table_data[1]
amazon_opening_price = amazon_data[1]
print(amazon_opening_price)

amazon_opening_price = table_data[1][1]
print(amazon_opening_price)

for row in table_data:
    ticker = row[0]
    closing_price = row[2]
    print(ticker, closing_price)


