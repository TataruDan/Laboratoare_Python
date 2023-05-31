import random as r
# Problem nr 6
elements = int(input("Insert the number of elements : ")) # read the number of elements
lst = []
for i in range(0,elements):
    lst.append(int(input())) # read the user elements and insert it into the list

print("Minimal value :", min(lst), "\nMax value :", max(lst)) # find min and max

# Problem nr 8
new_list = [] # create an empty list

for i in range(0,11):
    new_list.append(r.randint(1,10)) # generate random int number and insert it into the list

print("Initial list :", new_list)

print("Withouth duplicates :", list(set(new_list))) # using set, remove the duplicates , and after convert it to the list data type