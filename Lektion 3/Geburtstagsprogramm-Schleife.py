monate = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
while True:
    jahr = int(input("In welchen Jahr bist du geboren? "))
    monat = input("In welchem Monat bist du geboren? ")
    tag = int(input("Am wie vielten Tag hast du Geburtstag? "))

    try:
        monat = int(monat)
    except:
        try:
            monat = monat.index(monat) + 1
            
        except:
            print("Ungültige Eingabe\n\n")
            continue

    if tag == 20 and monat == 7:
        print("Herzlichen Glückwunsch.")
        print("Du bist", 2017 - jahr, "Jahre alt")
    if tag < 20 or tag > 20:
        print("Du hast heute nicht Gebrtstag")
        print("Du bist", 2017 - jahr, "Jahre alt")
        if jahr > 2017:
            print("Du hast geschum,mmelt, denn du kannst nicht unter Null Jahre alt sein")
            print("Bitte gebe diesmal dein richtiges Alter an")
        if jahr < 1900:
            print("Du hast geschumelt. Du kannst nicht über 100 Jahre alt sein. Ich weiß es einfach")
            print("Bitte geb diesmal dein richtiges Alter an")
                    
    antwort = input("\nWollen Sie noch einmal? (yes/no) ")
    
    if antwort != "yes":
        break
    
    else:
        print("\n\n")

        
