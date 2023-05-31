s="ProgramareaInteractiva"

# ex 1
print("First exercise : ")
print(s[:-1]) # returns string up to the length - 1 character
print(s[:1]) # returns the first character in the string
print(s[0:1]) # returns the first character in the string, it is equivalent to s[:1]
print(s[:]) # returns the whole string because by default it starts from 0 to size - 1a
print(s[-1:]) # returns the last character
print(s[2:5]) # returns the string from position 2 to position 4
print(s[-3:-1]) # returns a string from the -3 position till -1
print(s[1:9:2]) # returns a string, starting from position 1 to position 8 inclusive, with step 2
print(s[::-1]) # returns the initial string in reversed form
print("\n\n")

# ex 2
L = ['a','b','c','d','e']
print("Second exercise : ")
print(L[-1]) # return the last element from the list
print(L[:2]) # return first two elements from the list
print(L[:]) # return all elements from the list
print(L[1:3:2]) # returns only the second character from the list, because in the next step the position is equal to 3, therefore it is not executed
print(L[2:len(L)]) # returns the characters from position 2 to 4, because dim. total is 5
print(L[len(L) - 2]) # return the element from third position
print(L[1] + L[3]) # concatenation of two elements from the list
print(L[2] + L[-2]) # concatenation of two elements from the list
print(2 * L[2:4]) # a piece from the list appears 2 times
print(L[int(int('3'*2)/11)]) # return the element from third position
L[0:1]=['x','y'] # the first element in the list will be replaced by ['x','y']
L[0:2] = ['Python'] # The first and second elements will be replaced with the string 'Python'
print("\n\n")

#ex 3
print("Third exercise : ")
b=[34,45,56,38]
b.insert(-1,12) # insert a value before last element in the index
print(b)

b=[34,45,56,38]
b.pop() # pop the last element in the list
print(b)

b=[34,45,56,38]
b.remove(34) # remove the element from the mentioned position
print(b)

b=[34,45,56,38]
b.append('doi') # append the inserted value at the end of the list
print(b)

print(b.index('doi')) # return the index of the value

b=[34,45,56,38]
print(b.count(34)) # return the number of how many times the value appears in the list
b.reverse() # reverse the list
print(b)

b.sort() # sort in ascending order
print(b)

del(b[0:2]) # deleting the elements from position 0 and 1
print(b)

b.extend([1]) # adding the element at the end of the list
print(b)


