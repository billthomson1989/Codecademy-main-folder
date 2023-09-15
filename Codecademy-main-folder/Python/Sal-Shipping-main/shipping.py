# Weight variable declaration
weight = 41.5
cost_ground = 0
premium_ground = 125.00
cost_drone = 0
# Ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.0 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20


# Drone Shipping
if weight <= 2 :
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Ground Cost:" + " ", cost_ground)
print("Ground Premium:" + " ", premium_ground)
print("Drone Cost:" + " " ,cost_drone)

# Tests the code by manipulating the value of the weight variable according to your preference

  