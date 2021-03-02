# Input
x = float(input("Vneste x: "))
y = float(input("Vneste y: "))
z = float(input("Vneste z: "))

n = 0  #Broj brojeva koji pripada intervalu

if ( x >= 10 && x <= 100 ):
    n += 1
if ( y >= 10 && y <= 100 ):
    n += 1
if ( z >= 10 && z <= 100 ):
    n += 1

print(str(n) + " brojov je v intervale [10, 100]")