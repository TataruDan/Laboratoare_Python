
# First exercise
# Working with automatic convertation in Python
print("First exercise")
print("a) 2 / 5 = ", 2/5, " | Data type of the result : ", type(2/5), "|")
print("b) 7.9 + 1.1 = ", 7.9 + 1.1, " | Data type of the result : ", type(7.9 + 1.1), "|")
print("c) 6 - 2 = ", 6 - 2, "| Data type of the result : ", type(6 - 2), "|")
print("d) 8 + 1 = ", 8 + 1, "| Data type of the result : ", type(8 + 1), "|")
print("e) 9 + 1.1 =", 9 + 1.1, "| Data type of the result : ", type(9 + 1.1), "|")
print("f) 2 * 7 = ", 2 * 7, " | Data type of the result : ", type(2 * 7), "|")
print("g) 3.2 / 6 = ", 3.2 / 6, " | Data type of the result : ", type(3.2 / 6))
print("h) 5 * 8.0 = ", 5 * 8.0, " | Data type of the result : ", type(5 * 8.0))
print("i) 3.4 - 1.1 = ", 3.4 - 1.1, " | Data type of the result : ", type(3.4 - 1.1))
print("j) 9 % 2 = ", 9 % 2, "| Data type of the result : ", type(9 % 2))
print("k) 9 % -2 = ", 9 % -2, "| Data type of the result ", type(9 % -2))
print("l) -9 % 2 = ", -9 % 2, "| Data type of the result ", type(-9 % 2))

# Second exercise
print("\n\n")
print("Second exercise")
# The value that is equal to 0 or empty string will be equal with false, other values will be true
print(bool(-30))
print(bool(0.2))
print(bool(0))
print(bool('s'))

print("\n\n")

# Third exercise
print("Third exercise")
# Type convertion in Python
# Complex number
print(type(5.8e+3))
# Float number
print(type(1+4.0+2))
print(type(None))
print(type('float'))
# Complex number
print(type(4 + 2j))

print("\n\n")

# Fourth exercise
print("Fourth exercise")
x = 32
y = 6
# Modulus operator that help to get the remainder from the division
print("z = ", x % y + y)
print("z = ", x // y + x)
# Floor division return the result that is rounded down to the nearest whole number
print("y = ", x // y, "  z = ", x // y)
print("y = ", x // y + y, " z = ", x // y)

# Combination of mod and floor division
print("y = ", x % y + 2, "  z = ", x % y + x)
print("y = ", x // y, "  z = ", x % (y + 2))
print("y = ", x % y, "  z = ", x // (y + 2))

# Fifth exercise
print("\n\n")
print("Fifth exercise")

# Cast operator
print(12.5 / 2.5) # The data type of the result is float
print(int(12.5) / int(2.5)) # The data type of the result is float
print(int(12.5/2.5)) # After the division, the result is float, but cast operator transform it in integer data type

print("\n\n")
# Sixth exercise
print("Sixth exercise")

print(str(6) * int('5'))
print(int("6") + float("6.1"))
print(f"str(6) * float('6.1') - Error, because you cant multiply a string with float numbers")
print(str(6/4) * 2)

print("\n\n")

# Seventh exercise
print("Seventh exercise")
x = 3
y = 4

print(f"{x} + {y} = {x + y}")
print(f"({x})({y})")
print(f"x = {x}; y = {y}")
print(f"Răspuns : ({x})({y})")

# Eighth exercise
print("Eighth exercise")
f_value = input("Type first number : ")
s_value = input("Type second number : ")
def calculus(X, Y):
    return (pow(X,2)+pow(Y,2))*(pow((X-Y),2))

z = calculus(int(f_value),int(s_value))

print("Z = ",z)

# Nineth exercise

print("\n\n")
print("\n\n")
print("Nineth exercise")

val = int(input("Type the x value : "))
# Simple check if the value is in a specified range
if val < 0:
    print(val)
elif val >= 0 and val < 10:
    print(2 * val)
elif val >= 10 and val < 100:
    print(3 * val)
else:
    print(4 * val)
print("\n\n")

# Tenth exercise
print("Tenth exercise")
# The best way to check on duplicates, is to inserted data in set , because it don't allow duplicates
# and we just check the length of the original array with the set one.
def check_duplicates(array):
    return len(array) == len(set(array))


numbers = []

for x in range(4):
    numbers.append(int(input("Insert a number : ")))

if check_duplicates(numbers):
    print("There are no duplicates!")
else:
    print("There are duplicates in array!")


print("\n\n")
print("\n\n")

#Eleventh exercise
print("Eleventh exercise")
a = int(input("Firt number : "))
b = int(input("Second number : "))
c = int(input("Third number : "))

def check_numbers(a,b,c):
   if(a + b == c):
       print(c)
   elif (a + c == b):
       print(b)
   elif(b + c == a):
       print(a)
   else:
       print("There is no number that is sum of two other numbers")

check_numbers(a,b,c)