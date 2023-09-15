#string value of lovely_loveseat_description
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""

# price of lovely_loveseat
lovely_loveseat_price = 254.00

#string value of stylish_settee_description
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""

# price of stylish_settee
stylish_settee_price = 180.50

#string value of luxurious_lamp_description
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""

#price of luxurious_lamp
luxurious_lamp_price = 52.15
# sales tax value
sales_tax = .088

#customer purchases variable
customer_one_total = 0
#items bought by customer
#customer_one_itemization = ""

#customer purchases Lovely Loveseat
customer_one_total += 254.00
#update on customer_one_itemization
customer_one_itemization = lovely_loveseat_description 
#update on the total price of the purchases
customer_one_total += 52.15
#update on the items bought
customer_one_itemization += luxurious_lamp_description

#calculating customers sales tax
customer_one_tax = customer_one_total * sales_tax
#Adding to the total customer purchase
customer_one_total += customer_one_tax

#Printing our customer items and total price
print("Customer One Items:" + " " + customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)







