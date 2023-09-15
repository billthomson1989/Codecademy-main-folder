z_fighters = ['Goku','Vegeta','Gohan','Piccolo','Trunks']
print(z_fighters)

z_fighters = z_fighters + ['Goten']
print(z_fighters)

z_villians = ['Freeza','Cell','Buu','Omega Shenron']
z_dragons = ['Shenron','Porunga','Toronbo','B.Smoke Shenron']
print(z_villians + z_dragons)

z_fighters.insert(1, "Yamcha")
print(z_fighters)

del z_fighters[4]
print(z_fighters)

z_fighters.remove('Trunks')
print(z_fighters)

z_fighters = ['Goku','Vegeta','Gohan','Piccolo','Trunks']
for x in z_fighters:
    print(x)

z_fighters = ['Goku','Vegeta','Gohan','Piccolo','Trunks']
if "Vegeta" in z_fighters:
    print("Yes, Vegeta is a Z fighter")

print(len(z_fighters))


z_fighters = ['Goku','Vegeta','Gohan','Piccolo','Trunks']
print(z_fighters)

