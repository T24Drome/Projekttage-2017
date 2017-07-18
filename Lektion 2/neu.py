jahr = int(input("In welchen Jahr bist du geboren? "))
monat = int(input("in welchem Monat (als Zahl) bist du geboren? "))
tag = int(input("Am wie vielten Tag hast du Geburtstag? "))

if tag == 18 and monat == 7:
    print("herzlichen Glückwunsch. Happy birthday to you :D")
    print("Du bist", 2017 - jahr, "Jahre alt")
elif monat > 7 or monat < 7:
    print("du hast heute nicht Geburtstag")
    print("du bist", 2017 - jahr, "Jahre alt")
if jahr > 2017:
    print("du hast geschummelt, denn du kannst nicht unter Null Jahre alt sein")
