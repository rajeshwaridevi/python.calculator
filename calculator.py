
print("Welcome")

a = int(input("Enter a value 1: "))
b = int(input("Enter a value 2: "))

sign = input("Enter a sign : ")

if sign == "+":
    print(a + b)

elif sign == "-":
    print(a - b)

elif sign == "*":
    print(a * b)

elif sign == "/":
    print(a / b)

elif sign == "%":
    print(a % b)
elif sign =="**":
    print(a**b)

else:
    print("Invalid sign")

