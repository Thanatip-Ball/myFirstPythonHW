def A ():
    print("********************************************************************")
    print("*                            MENU OIL                              *")
    print("*                 1.Gasoline 95  Price 29.16 Baht                  *")
    print("*                 2.Gasoline 91  Price 25.30 Baht                  *")
    print("*                 3.Gasohol  91  Price 21.68 Baht                  *")
    print("*                 4.Gasohol E20  Price 20.2  Baht                  *")
    print("*                 5.Gasohol  95  Price 21.2  Baht                  *")
    print("*                 6.Diesel       Price 21.1  Baht                  *")
    print("********************************************************************")

def sub():
    a = input("Select 1.price to liter or 2.liter to price : ")
    pricetoliter = "1"
    litertoprice = "2"
    b = input("Select oil 1-6 : ")
    if pricetoliter in a:
        print("price : ")
    elif litertoprice in a:
        print("liter : ")
    c = int(input())
    d = a.upper()
    e = 0
    if pricetoliter in a:
        if "1" in d:
            e = e + (c/29.16)
            print("oil", '%.2f' %e, "liter")
        elif "2" in d:
            e = e + (c/25.30)
            print("oil", '%.2f' %e, "liter")
        elif "3" in d:
            e = e + (c/21.68)
            print("oil", '%.2f' %e, "liter")
        elif "4" in d:
            e = e + (c/20.2)
            print("oil", '%.2f' %e, "liter")
        elif "5" in d:
            e = e + (c/21.2)
            print("oil", '%.2f' %e, "liter")
        elif "6" in d:
            e = e + (c/21.1)
            print("oil", '%.2f' %e, "liter")
        else:
            print("Invalid information, plase Enter again")
    elif litertoprice in a:
        if "1" in d:
            e = e + (c * 29.16)
            print("price", e, "Baht")
        elif "2" in d:
            e = e + (c * 25.30)
            print("price", e, "Baht")
        elif "3" in d:
            e = e + (c * 21.68)
            print("price", e, "Baht")
        elif "4" in d:
            e = e + (c * 20.2)
            print("price", e, "Baht")
        elif "5" in d:
            e = e + (c * 21.2)
            print("price", e, "Baht")
        elif "6" in d:
            e = e + (c * 21.1)
            print("price", e, "Baht")
        else:
            print("Invalid information, plase Enter again")
    else:
        print("plase Enter again")

def lop():
    print("Enter to back the menu")
    F = "0"
    E = input()
    while True:
     if F == E:
         print("\nThank You")
         break
     if F != E :
            A()
            sub()

A()
sub()
lop()


