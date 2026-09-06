#Build a number-base converter supporting binary, decimal, octal, and hexadecimal.

#Used 
text = input("Number: ")

base = int(input("What is base of number (2, 8, 10, 16): "))

number = int(text, base)

print("Binary: ", bin(number))
print("Octal: ", oct(number))
print("Decimal: ", number)
print("Hexadecimal: ", hex(number))