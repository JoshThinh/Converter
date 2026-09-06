#Build an ASCII-to-decimal converter.

#In class code
s = "Joshua"

for c in s: 
    print(ord(c))

#Pythonic way
print(",".join(str(ord(c)) for c in s))