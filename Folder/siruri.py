# Problem nr. 3
# Eliminate , character from the string in 2 different ways
S = "st,ri,ng"
W = "st,ri,ng"

# First way

print("Before modification : ",S , " | ", " After modification : ",S.replace(",","")) # replace the "," character from the string

# Second way
print("Before modification : ",W , " | ", " After modification : ",W.translate({ord(",") : None})) # replace the "," character from the string with None value

# Problem nr. 11
number = input("Insert a number : ") # get a number in string format
h = list(number) # make a list from this string
print("Sliced number :", int("".join(h[1:-1]))) # remove the first and the last element and join it
