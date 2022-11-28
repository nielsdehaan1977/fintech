"""Racking up the profit."""

# Suppose each stock price is the same
stock_price = 30

# But that dividend yields vary across five stocks in your portfolio
dividend_yields = [0.035, 0.040, 0.072, 0.012, 0.052]

# @TODO: Create a variable to hold tallied dividend income
total_dividend_income = 0.0


# @TODO: Create a for loop to calculated and add up all the dividend income
for div in dividend_yields:
    dividend_per_share = stock_price * div
    total_dividend_income = total_dividend_income + dividend_per_share

    print("Your dividend will be: ", dividend_per_share)

# @TODO: Once it's all done, print the dividend income for the entire portfolio
print("Total dividend received is: ", total_dividend_income)
