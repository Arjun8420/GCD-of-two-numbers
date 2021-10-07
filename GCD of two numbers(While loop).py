#Program to calculate the GCD of two numbers

a = int(input("Enter first Number = "))
b = int(input("Enter second Number = "))

while (b != 0) :
    temp = a%b
    a = b
    b = temp
print("GCD =",a)
