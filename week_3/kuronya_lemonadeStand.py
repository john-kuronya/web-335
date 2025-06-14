"""
Author: John Kuronya
Date: 2025-06-09
File Name: kuronya_lemonadeStand.py
Description: Program calculates the cost of making lemonade and the profit from selling it.
"""

# Function to calculate the total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    # Add the cost of lemons and sugar to get total cost
    return lemons_cost + sugar_cost

# Function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    # Subtract the total cost from the selling price to get profit
    total_cost = calculate_cost(lemons_cost, sugar_cost)
    return selling_price - total_cost

# --- Test Variables ---
lemons_cost = 3.00     # Cost of lemons in dollars
sugar_cost = 2.00      # Cost of sugar in dollars
selling_price = 10.00  # Selling price of lemonade in dollars

# --- Calculate Cost and Profit ---
total_cost = calculate_cost(lemons_cost, sugar_cost)
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

# --- Build Output Strings ---
cost_output = "$" + str(lemons_cost) + " + $" + str(sugar_cost) + " = $" + str(total_cost)
profit_output = "Selling at $" + str(selling_price) + " gives a profit of $" + str(profit)

# --- Print Results ---
print("Cost of making lemonade:")
print(cost_output)
print("\nProfit from selling lemonade:")
print(profit_output)
