import math

# Unesemo vrednosti
a = float(input("Unesi vrednost a "))
b = float(input("Unesi vrednost b "))
c = float(input("Unesi vrednost c "))

# Proverujemo pravougaonost
a2 = math.sqrt(b**2 + c**2)
b2 = math.sqrt(a**2 + c**2)
c2 = math.sqrt(a**2 + b**2)
print((c2) or (a2) or (b2))
if ((c == c2) or (a == a2) or (b == b2)):
    # Ako je ovo tacno trougao je pravougaoni i izracunavamo njegovu povrsinu
    print("Trougao je pravougaoni")
if (c == c2):
    povrsina = (a*b/2)
    print("Povrsina trougla je" , povrsina)
if (a == a2):
    povrsina = (c*b/2)
    print("Povrsina trougla je" , povrsina)
if (b == b2):
    povrsina = (a*c/2)
    print("Povrsina trougla je" , povrsina)
else:
    # Ako nije nista od toga onda trougao nema pravi ugao
    print ("Trougao nije pravougli")
