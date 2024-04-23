
a = 1

n = int(input("Entra numero enter: "))

while n > 0:
    
    for i in range(1,n+1):
        a *= i

    print("\nEl factorial d'aquest numero es:", a)
    a = 1
    n = int(input("Entra numero enter: "))