day = int(input("enter your birthday: "))
month = int(input("enter your birth month: "))
year = int(input("enter 2 digit birth year: "))

magicdate = month * day

if magicdate == year:
    print("Wow so magical!: ")
elif day > 31 or day < 1:
    print("error")
else:
    print("Ehh nothin' special")
