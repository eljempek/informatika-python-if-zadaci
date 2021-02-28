# Input
x = float(input("Vneste x: ")) 
y = float(input("Vneste y: "))
z = float(input("Vneste z: "))

# Provera da li moze da se konstruise trougao
# Ovo su tri uslova za validnost trougla:
# 1.a + b > c 
# 2.a + c > b 
# 3.b + c > a
if ((x + y > z) and (x + z > y) and (y + z > x)):
    # Trougao je validan
    if (x == y == z):
        # Trougao je jednakostranicni
        print("trougao je jednakostranicni")
    elif ((x == y) or (x == z) or (y == z)):
        # Trougao je jednakokraki
        print("the bitch is jednakokraki")
    else:
        # Trougao je raznostranicni
        print("trougao je raznostranicni")
else:
    # Trougao belongs to dem streets
    print("the bitch aint valid she belong to the streets5")