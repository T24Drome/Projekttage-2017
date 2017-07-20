    #Addierer mit +=1
zahl1 = int(input("Zahl1: "))
zahl2 = int(input("Zahl2: "))
print("Das hier ist ein Addierer also der Rechner rechnet nur Plus!\n")

ergebnis = 0

i = 0
if zahl1 > 0:
    i = 0
    while i < zahl1:
        ergebnis += 1
        i += 1
else:
    i = 0
    while i > zahl1:
        ergebnis -= 1
        i -= 1

if zahl2 > 0:
    i = 0
    while i < zahl2:
            ergebnis += 1
            i += 1
else:
    i = 0
    while i > zahl2:
        ergebnis -= 1
        i -= 1

        
        print("Ergebnis:", ergebnis)
