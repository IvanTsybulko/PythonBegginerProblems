import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a!= 0 and b!= 0 and c!= 0:
    if (b**2) - 4*a*c > 0:
        print((-b + math.sqrt(b**2 - 4*a*c))/(2*a))
        print((-b - math.sqrt(b**2 - 4*a*c))/(2*a))

    else:
        print(-c/b)
elif b!= 0:
    print(-c / b)
else:
    print("Nqma koreni")
