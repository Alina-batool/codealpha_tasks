# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

# Variable to store the total investment value
total_investment = 0

print("=== Stock Portfolio Tracker ===")

# Ask the user how many different stocks they own
num_stocks = int(input("Enter the number of different stocks: "))

# Loop through each stock
for i in range(num_stocks):

    # Get stock name from the user
    stock_name = input("\nEnter stock symbol (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    # Check if the stock exists in the dictionary
    if stock_name in stock_prices:

        # Get quantity of shares
        quantity = int(input("Enter quantity: "))

        # Calculate investment for this stock
        investment = stock_prices[stock_name] * quantity

        # Add to total investment
        total_investment += investment

    else:
        print("Stock not found. Skipping...")

# Display total investment value
print("\nTotal Investment Value: $", total_investment)

# Optional: Save the result to a text file
save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")
    file.write("Total Investment Value: $" + str(total_investment))
    file.close()
    print("Result saved to portfolio.txt")
else:
    print("Result not saved.")