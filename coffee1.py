water = 400
milk = 540
coffeebeans = 120
cups = 9
money = 550


def print_out(): #หน้าบอกว่าวัตถุดิบมีเท่าไร
    print("The coffee machine has : ")
    print(water, " of water ")
    print(milk, " of milk ")
    print(coffeebeans, " of coffee beans ")
    print(cups, " of cups ")
    print(money, " of money ")
    print()


def p2():
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 36 + "1.Buy" + " " * 36 + "#")
    print("#" + " " * 36 + "2.Fill" + " " * 36 + "#")
    print("#" + " " * 36 + "3.Take" + " " * 36 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)


print_out() #เลือก buy,fill,take
a = input("Enter")
check = True
while check:
    p2()
    s = input("Select 1-3 : ")
    if s == '1': #กด 1 เท่ากับซื้อ เลือกชนิดกาแฟ
        print("What do you want coffee? 1 - espresso, 2 - latte, 3 - cappuchino:")
        c = int(input(": "))
        print()
        if c == 1:
            water -= 250
            coffeebeans -= 16
            money += 4
        elif c == 2:
            water -= 350
            milk -= 75
            coffeebeans -= 20
            money += 7
        elif c == 3:
            water -= 200
            milk -= 100
            coffeebeans -= 12
            money += 6
        cups -= 1
        print_out()
        print()
        break
    elif s == '2': #กด 2 เท่ากับเติมของ ใส่ปริมาณของวัตถุดิบ
        print("How many ml of water do you want to add : ")
        water += int(input(": "))
        print("How many ml of milk do you want to add : ")
        milk += int(input(": "))
        print("How many grams of coffee beans do you want to add : ")
        coffeebeans += int(input(": "))
        print("How many disposable cups of coffee do you want to add : ")
        cups += int(input(": "))
        print()
        print_out()
        print()
        break
    elif s == '3': #กด 3 เท่ากับเก็บเงิน เก็บทั้งหมด
        print("I gave you $550")
        money = 0
        print()
        print_out()
        print()

        break

