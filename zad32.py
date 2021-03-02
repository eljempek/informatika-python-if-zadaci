<<<<<<< HEAD
# Koliko od tri broja x,y,z pripada intervalu [10, 100]
x = int(input("Vneste x "))
y = int(input("Vneste y "))
z = int(input("Vneste z "))
n = 0
if(x > 10 and x < 100):
    n = 1
if(y > 10 and y < 100):
    n = 1 + n
if(z > 10 and z < 100):
    n = 1 + n
print(str(n) + " brojov je v intervale [10, 100]")

    
=======
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
>>>>>>> 98317338a5dd15a67313b698fc97025954d9ee13
