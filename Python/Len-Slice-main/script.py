# Your code below:
# Kinds of pizza
toppings = ["pepperoni", "pineapple", "cheese",
            "sausage", "olives", "anchovies", "mushrooms"]

# Prices of pizza
prices = [2, 6, 1, 3, 2, 7, 2]

#num of $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#  length of toppings list
num_pizzas = len(toppings)

#printing to the console
print("We sell", num_pizzas, "different kinds of pizza!")

# Two dimensional list
pizza_and_prices = [[2,	"pepperoni"], [6,	"pineapple"], [1,	"cheese"], [
    3, "sausage"], [2,	"olives"], [7,	"anchovies"], [2,	"mushrooms"]]


# sorting the pizza_and_prices table
pizza_and_prices.sort()

# the most Cheapest pizza
cheapest_pizza = pizza_and_prices[0]

# the most expensive pizza
priciest_pizza = pizza_and_prices.pop()

# Removing the most expensive pizza after purchase
bought_exp_pizza = pizza_and_prices[-1:]

# Inserting new toppings in accordance of our sorted list
pizza_and_prices.insert(4, [2.5, "peppers"])

# Three lowest cost
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
