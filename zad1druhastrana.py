print ("Unesite broj a")
a = int(input())
print ("Unesite broj b")
b = int(input())
if (b<0):
    if (a<0):
        z=a*(-1)
    else:
        z=a
elif (b==0):
    z==0
else:
    z=a*a
print ("z=" , z)