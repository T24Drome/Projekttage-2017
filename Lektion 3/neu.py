while True:
    jahr = int(input("In welchen Jahr bist du geboren? "))
    monat = int(input("In welchem Monat (als Zahl) bist du geboren? "))
    tag = int(input("Am wie vielten Tag hast du Geburtstag? "))


    if tag == 19 and monat == 7:
        print("Herzlichen Glückwunsch. Hoffentlich gehts dir gut")
        print("Du bist", 2017 - jahr, "Jahre alt")
    if tag < 19 or tag > 19:
        print("Du hast heute nicht Gebrtstag")
        print("Du bist", 2017 - jahr, "Jahre alt")
    if jahr > 2017:
        print("Du hast geschummelt, denn du kannst nicht unter Null Jahre alt sein")
        print("Bitte gebe diesmal dein richtiges Alter an")
    if jahr < 1900:
        print("Du hast geschumelt. Du kannst nicht über 100 Jahre alt sein. Ich weiß es einfach")
        print("Bitte geb diesmal dein richtiges Alter an")
                    
    antwort = input("\nWollen Sie noch einmal? (yes/no) ")
    
    if antwort != "yes":
        break
    else:
        print("\n\n")
