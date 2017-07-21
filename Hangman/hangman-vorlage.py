# Hangman


from hangman_renderer import render_hangman


def convert_upper_case(string):
    if "ß" in string:
        chars = []
        for char in string:
            if char == "ß":
                chars.append("ß")
            else:
                chars.append(char.upper())
        return "".join(chars)
    else:
        return string.upper()


def spielmodus_fragen():
    # Benutzer nach Spielmodus fragen (Einzel/Multi)
    antwort = input("Wähle einen Spielmodus Einzel/Multi spielen? ")
    if antwort == "Einzel":
    
    # Falls Einzelspieler gewählt wurde folgenden Code ausführen
        worte = ["Schmetterling", "Schokokuchen", "Kuhmist", "Faupax", "Rhythmus", "Rhesusfaktor", "Physiognomie", "Jazz", "Fahrradkette", "Steppe"]
        # hier kannst du noch mehr Wörter einfügen

        import random
        return worte[random.randint(0, len(worte) - 1)]     # diese zwei Zeilen sorgen für die zufällige Auswahl

    else:
        while True:
        # Falls Mehrspieler gewählt wurde folgenden Code ausführen
            # Endlosschleife 
                # eigenes Wort vom Spieler erhalten
                spielerwort = input("gebe hier dein Wort ein für den anderen Spieler.")
                # prüfen ob das Wort nur aus Buchstaben besteht: eingabe.isalpha()
                if spielerwort.isalpha():
                    return spielerwort
                else:
                    print("\nUngültige Eingabe!")
                    # wenn ja zurückgeben
                if True:
                    print("Gut gemacht. Du hast ein Wort für deinen Mitspeiler eingegeben.")
                    print("Du hast ingesamt 6 Fehlversuche")
                   
                    # Meldung ausgeben, Endlosschleife fortsetzen
                    print("nun bist du in Hangman. Viel Glück")

                    

def zeichne_spiel():
    global falsche_buchstaben, meldung, erratenes_wort, fehlversuche
    print("\n" * 100)       # 100 leere Zeilen, damit der Bildschirm "leer" ist

    render_hangman(fehlversuche)    # zeichnet den Hangman abhängig der bisherigen Fehlversuche

    # falsche Buchstaben ausgeben

    # convert_upper_case(", ".join(falsche_buchstaben)) erzeugt den auszugebenden Text
    print("Falsche Buchstaben: " + convert_upper_case(", ".join(falsche_buchstaben)))
    
    # Meldung ausgeben
    print(meldung)
    # bisher erratenes Wort ausgeben
    
    # convert_upper_case(" ".join(erratenes_wort)) erzeugt den auszugebenden Text
    print(convert_upper_case(" ".join(erratenes_wort)))


def rate_buchstabe():
    global übrige_buchstaben, meldung
    # Buchstabe vom Spieler eingeben lassen, Eingabe in Kleinbuchstaben konvertieren
    buchstabe = input("\nRaten sie einen Buchstaben ").lower()


# wenn die Länge der Eingabe nicht gleich eins ist, False zurückgeben
    if len (buchstabe) != 1:
        return False
    
# wenn die Eingabe kein Buchstabe ist, False zurückgeben
#if buchstabe not in list("abcdefghijklmnopqrstuvwxyzäöüß"):
    if buchstabe not in list("abcdefghijklmnopqrstuvwxyzäöüß"):
        return False       #return False

# wenn die Eingabe nicht bei den übrigen Buchstaben ist, False zurückgeben
#elif buchstabe not in übrige_buchstaben:
    if buchstabe not in übrige_buchstaben:

    #return False
        return False
# wenn noch nichts zurückgegeben wurde, den eingegebenen Buchstaben zurückgeben
    return buchstabe

def eingabe_auswerten(buchstabe):
    global fehlversuche, falsche_buchstaben, übrige_buchstaben, meldung, wort, erratenes_wort

# wenn der Buchstabe im Wort vorkommt
    if buchstabe in wort:
        for i in range(len(wort)):
#jede Stelle des Wortes durchgehen und schauen ob da der eingegebene Buchstabe steht
            if wort[i] == buchstabe:
# falls ja, dann im erratenen Wort ebendiese Stelle durch den Buchstaben ersetzen
                erratenes_wort[i] = buchstabe
        meldung = "Gut gemacht"
# Buchstabe von den übrigen Buchstaben entfernen
        übrige_buchstaben.remove(buchstabe)


    # ansonsten
    else:
        # Anzahl der Fehlversuche um eins erhöhen
        fehlversuche += 1
        # Buchstabe zu den falsche Buchstaben hinzufügen
        falsche_buchstaben.append(buchstabe)
        # Buchstabe von den übrigen Buchstaben entfernen
        übrige_buchstaben.remove(buchstabe)
    # wenn kein "_" mehr im bereits erratenen Wort vorkommt
    #if "_" not in erratenes_wort:
    if "_" not in erratenes_wort:
        # Meldung über gewonnenes Spiel setzen
        print("Sie gewinnen ahhh")
        #return True

        return True

    if fehlversuche == 6:
    # wenn bereits sechs Fehlversuche gemacht wurden
        # Meldung über Niederlage setzen
        print("Du hast verloren")
        #return True
        return True
    # wenn noch nichts zurückgegeben wurde, False zurückgeben
    

print("\n" * 100)
print("=== H A N G M A N ===\n\n\n")

while True:

    
    fehlversuche = 0         # Anzahl der Fehlversuche auf null setzen

    falsche_buchstaben = []   # falsche Buchstaben als leere Liste setzen

    übrige_buchstaben = list("abcdefghijklmnopqrstuvwxyzäöüß")      # erzeugt eine Liste mit allen Buchstaben

    meldung = ("")

    wort = spielmodus_fragen().lower()                 # Funktion spielmodus_fragen() aufrufen um Wort zu erhalten, Wort in Kleinbuchstaben konvertieren

    erratenes_wort = ["_"] * len(wort)      # erzeugt eine Liste mit so vielen "_" wie das Wort lang ist
    
    while True:

        zeichne_spiel()
        # Funktion rate_buchstabe() aufrufen um geratenen Buchstaben zu erhalten
        buchstabe = rate_buchstabe()
        # falls False zurückgegeben wurde, Schleife von vorne beginnen (continue)
        if buchstabe :
            if eingabe_auswerten(buchstabe):
                break
        # andernfalls eingabe_auswerten(buchstabe) aufruf
        # falls dies True zurückgibt, Schleife abbrechen (break)
       
    # am Ende des Spiels noch einmal neu zeichnen mit der Funktion zeichne_spiel()
    zeichne_spiel()
    print("\n\n")
    
    antwort = input("\nWollen Sie noch einmal? (yes/no) ")
    
    if antwort != "yes":
        break
    else:
        print("\n\n")
