hairstyles = ["bouffant", "pixie", "dreadlocks",
              "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# task 1
total_price = 0
# task 2
for price in prices:
  total_price += price
# task 3
average_price = total_price / len(prices)
# task 4
print("Average Haircut Price:")
print(average_price)
# task 5
new_prices = [price-5 for price in prices]
# task 6
print(new_prices)
# task 7
total_revenue = 0
# task 8
for i in range(len(hairstyles)):
  #task 9
  total_revenue += prices[i]*last_week[i]
  # task 10
print("Total Revenue:", total_revenue)

# task 11
average_daily_revenue = total_revenue / 7

# task 12
cuts_under_30 = [hairstyles[i]
                 for i in range(len(hairstyles)) if new_prices[i] < 30]
# task 13
print(cuts_under_30)
