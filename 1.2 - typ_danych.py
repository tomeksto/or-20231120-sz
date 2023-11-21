while True:
    print("To jest program typu: KALKULATOR")
    print("Działania:")
    print("mnozenie: *")
    print("dzielenie: /")
    print("dodawanie: +")
    print("odejmowanie: -")
    print("inny znak wyjscie z programu")
    znak = input("Podaj typ działania: ")

    match znak:
        case "*":
            print("Wybrałeś mnożenie")
        case "/":
            print("Wybrałeś dzielenie")
        case "+":
            print("Wybrałeś dodawanie")
        case "-":
            print("Wybrałeś odejmowanie")
        case _ :
            print("Wybrałeś wyjście z programu")
            break

    while True:
        liczba1 = input("Podaj pierwszą liczbę")
        if liczba1.isnumeric():
            break

    while True:
        liczba2 = input("Podaj drugą liczbę")
        if liczba2.isnumeric():
            break

    wynik = liczba1 liczba2
