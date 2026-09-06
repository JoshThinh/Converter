#Build a number-base converter supporting binary, decimal, octal, and hexadecimal.

#User inputs the number they want to convert
text = input("Number: ")

#User enters the base value that the number is in
base = int(input("What is base of number (2, 8, 10, 16): "))

#converts to int
number = int(text, base)

#prints out the number in different bases
print("Binary: ", bin(number))
print("Octal: ", oct(number))
print("Decimal: ", number)
print("Hexadecimal: ", hex(number))