#Kinetic Energy calculator

def kinetic_energy():
    m = int(input("What is the weight: "))
    v = int(input("What is thhe velocity: "))
    KE(m, v)

def KE(m, v):
    result = 1/2*m*v*2
    print(result)

kinetic_energy()
