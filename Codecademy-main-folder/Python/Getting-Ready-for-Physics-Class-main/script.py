# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:

# task 1
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp


# task 2
f100_in_celsius = f_to_c(32)
print(f100_in_celsius)

# task 3


def c_to_f(c_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp


# task 4
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# task 5


def get_force(mass, acceleration):
  return mass * acceleration


# task 6
train_force = get_force(train_mass, train_acceleration)
# task 7
print("The GE train supplies" + " " +
      str(train_force) + " " + "Newtons of force.")
# task 8


def get_energy(mass, c=3*10**8):
  return (mass * c ** 2)


# task 9
bomb_energy = get_energy(bomb_mass)
# task 10
print("A 1kg bomb supplies" + " " + str(bomb_energy) + " " + "Joules.")

# task 11


def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance


# task 12
train_work = get_work(train_mass, train_acceleration, train_distance)
# task 13
print("The GE train does" + " " + str(train_work) + " " +
      "Joules of work over" + " " + str(train_distance) + " " + "meters")
