#Olaide Bamisile
#mass and weight
mass = float(input("Enter the weight: "))

weight = mass * 9.8

print(weight)

if weight > 500:
    print("too heavy")
elif weight < 100:
    print("too light")
else:
    print("just right")
