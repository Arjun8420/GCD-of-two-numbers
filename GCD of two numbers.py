#Program to calculate the GCD of two numbers

a = int(input("Enter first Number = "))
b = int(input("Enter second Number = "))

while (a != b) :
    if (a>b) :
        a -= b
    else:
        b -= a

print("GCD =",a)
