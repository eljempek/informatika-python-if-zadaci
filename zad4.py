# Funkcija koja odredjuje dijagonalu
def diag(a):
    return sqrt(2 * pow(a, 2))

# Input
a1 = float(input("Unesite stranicu a1: "))
a2 = float(input("Unesite stranicu a2: "))

# Kalkulisati dijagonale za svaki od kvadrata
d1 = diag(a1)
d2 = diag(a2)

if (d1 > d2):
    # Dijagonala d1 je veca od d2
    print("Dijagonala d1 je veca od d2")
elif (d2 == d2):
    # Dijagonale su iste
    print("Dijagonale su iste")
else:
    # Dijagonala d2 je veca od d1
    print("Dijagonala d2 je veca od d1")