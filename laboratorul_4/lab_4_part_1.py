# Defined class that represent a stack

import pickle

class Stack: # main class
    def __init__(self): # constructor
        self.items = []

    def isEmpty(self): # check if stack is empty
        return self.items == []

    def push(self, item): # push new elements at the end of the stack
        return self.items.append(item)

    def pop(self): # pop the last element of the stack
        return self.items.pop()

    def peek(self): # return the last element of the stack
        return self.items[len(self.items) - 1]

    def size(self): # return the size of the stack
        return len(self.items)

    def __str__(self): # convert to string elements of the stack
        return 'Stack(items : ' + str(self.items) + ')'

    def save(self,filename): # save information into a binary file
        with open(filename,'wb') as information:
            pickle.dump(self.items,information)

    def load(self,filename): # get the information from a binary file
        with open(filename,'rb') as information:
            self.items = pickle.load(information)

        print(self.items)

# initialise a new stack
m = Stack()
# push elements into the stack
m.push(1)
m.push(3)
print("First stack : " + str(m.items))
# initialise another stack
s = Stack()
# push elements into the stack
s.push(42)
s.push(12)

print("Second stack : " + str(s.items))

# create a stack container
class Stack_Container:
    def __init__(self): # create constructor
        self.items = []

    def __getitem__(self,index): # print the information about the x element in position [index]
        print("The position is " + self.items[index])

    def add(self,stack): # add new info into the container
        return self.items.append(stack)

    def show_data(self): # show the container's info
        return self.items

    def remove(self,index): # remove data from container
        return self.items.pop(index)

    def save(self, filename): # save data into a binary file
        with open(filename, 'wb') as information:
            pickle.dump(self.items, information)

    def load(self, filename): # read data from a binary file
        with open(filename, 'rb') as information:
            self.items = pickle.load(information)

        print(self.items)

# initialise a container
container = Stack_Container()
# insert info into the container
container.add(m.items);
container.add(s.items);
container.remove(1)
# show data from the container
print("Container : " + str(container.show_data()))