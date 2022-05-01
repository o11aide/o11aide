#Stadium Seating

def main():
    classA()
    classB()
    classC()

def classA():
    ticketa = 10.00
    ticket1 = float(input("How many tickets were sold for class C: "))
    total1 = ticket1 * ticketa
    print("the total is $", total1,".")

def classB():
    ticketb = 15.00
    ticket2 = float(input("How many tickets were sold for class B: "))
    total2 = ticket2 * ticketb
    print("the total is $", total2,".")

def classC():
    ticketc = 20.00
    ticket3 = float(input("How many tickets were sold for classs A: "))
    total3 = ticketc * ticket3
    print("the total is $", total3,".")

main()
