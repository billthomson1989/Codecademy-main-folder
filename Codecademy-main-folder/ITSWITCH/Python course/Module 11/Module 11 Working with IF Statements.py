x=1
y=3
if x>y:
    print("X is greater than Y")

print("-----------------------------------------")

x=33
y=33
if x>y:
    print("X is greater than Y")
elif x==y:
    print("X and Y are equal")    
else:
    print("Y is greater than X")


print("-----------------------------------------")


x=20
y=10
if x>y: print("x is greater than y")


a=8
b=2
print("A is greater") if a>b else print("B wins")


print("-----------------------------------------")

requested_options = ['leather', 'sun roof'] #alarm is not included, thus the statement was skipped.

if 'leather' in requested_options:
    print("Nice leather interior")
if 'alarm' in requested_options:
    print("Keeping the bad guys away!")
if 'sun roof' in requested_options:
    print("Letting the sun in")

print("\nFinished making your car!")
    


print("-----------------------------------------")

Scottish_weather = ['19 degrees', 'wet'] #sleet was skipped, so python automatically skipped the statement about hot toddies.

if '19 degrees' in Scottish_weather:
    print("Taps aff!")
if 'sleet' in Scottish_weather:
    print("Time for a hot toddy, son!")
if 'wet' in Scottish_weather:
    print("Get yer wellies oot!")

print("\nBest just not to go outside")



