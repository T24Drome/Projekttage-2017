print("Hallo und willkommen bei Deutschlands berühmtester Quizshow.")
print("Dann fackeln wir nicht lange sondern fangen gleich an.")
print("Frage Nr.1: Wie heißt das Spiel mit den meisten Waffen?")
print("a: Call of Duty. b: Borderlands. c: battlefield oder d: red dead redemption?")
antwort1 = input("a, b, c oder d.")

if antwort1 == "b":
    print("Die richtige Antwort ist ... b!!!")
    print("nicht schlecht. Doch das war erst die Erste von Vier Fragen.")
    print("kommen wir zur nächsten Frage.")
    print("Frage Nr2: Was für eine Hunderasse gibt es NICHT?")
    print("a: Labrador, b: Dackel, c: Dalmatiner oder d: Bengal?")
    antwort2 = input("a, b, c, oder d?")
else:
    print("ohh schade. Leider die falsche Antwort.")
    
if antwort2 == "d":
    print("Und d ist... RICHTIG!")
    print("Nagut, bis jetzt waren die Fragen noch ´einfach´. Doch jetzt kommen die Elite Fragen.")
    antwort = input("Bist du bereit für die nächste Frage und gleichzeitig vorletzte Frage?")
    if antwort == "nein":
        print("ach das ist schade:(. Dann versuchs irgendwann anders nochmal.")
    if antwort == "ja":
        print("Gut dann kommen wir zur vorletzten Frage")
        print("Frage Nr.3: 
