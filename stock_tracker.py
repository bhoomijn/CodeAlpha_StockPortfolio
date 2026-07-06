# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOG": 2800
}

portfolio = {}
total_value = 0

print("Welcome to Stock Portfolio Tracker!")

# User input loop
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    else:
        print("Stock not found in database!")

# Calculate total value
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares → ${value}")

print(f"\nTotal Portfolio Value: ${total_value}")

# Save to file
with open("portfolio.txt", "w") as f:
    f.write("Stock Portfolio Report\n")
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}\n")
    f.write(f"\nTotal Portfolio Value: ${total_value}\n")

print("\nPortfolio saved to portfolio.txt ✅")
