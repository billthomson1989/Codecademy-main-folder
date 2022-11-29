outer = ['outer1','outer2','outer3']
nest = ['nest1','nest2','nest3']

for x in outer:
    for y in nest:
        print(x,y)
    print("\n")

numbers = [1,2,3]
letters = ['a','b','c']

for x in numbers:
    print(x)
    for y in letters:
        print(y)
    print("\n")


print("---------------------------------------------")
#module 14 practice


Movies = ['Matrix','Shawshank','Jaws']
Actors = ['Keanu','Freeman','The Shark', 'The Robots','The Prisoners']

for x in Movies:
    print(x)
    for y in Actors:
        print(y)
    print("\n")


Movie = ['Matrix']
Characters = ['Neo','Morpheus','Trinity','Agent Smith','The Oracle']

for a in Movie:
    print(a)
    for b in Characters:
        print(b)
    print("\n")


Anime = ['Dragonball']
Main_Characters = ['Goku','Gohan','Vegeta', 'Piccolo','Trunks']

for c in Anime:
    print(c)
    for d in Main_Characters:
        print(d)
    print("\n")


Music = ['Blues']
Songs = ['The Thrill is gone','Key to the Highway','Stop the Rain', 'Stars','She Caught the Katie']

for e in Music:
    print(e)
    for f in Songs:
        print(f)
    print("\n")
