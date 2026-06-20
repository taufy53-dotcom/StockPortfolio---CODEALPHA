# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420
}

total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

num_stocks = int(input("\nHow many stocks do you own? "))

for i in range(num_stocks):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"{stock_name} Investment = ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Portfolio Value = $", total_investment)

# Optional: Save to file
save = input("Save result to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write(f"Total Portfolio Value = ${total_investment}")

    print("Result saved in portfolio.txt")