# the list declaration that will stock all 8 dictionaries
BOOK = []
# Inserting data into the dictionaries then insert them into the list
for i in range(0,8):
    ZNAK = {"NAME" : None, "ZODIAC" : None, "BDAY" : [None,None,None]}
    ZNAK["NAME"] = input("Insert Your Name and Surname : ")
    ZNAK["ZODIAC"] = input("Insert your zodiac sign : ")
    print("\nInsert data of birth : \n")
    ZNAK["BDAY"][0] = int(input("Insert year : "))
    ZNAK["BDAY"][1] = int(input("Insert month : "))
    ZNAK["BDAY"][2] = int(input("Insert day : "))
    # Appending data to the list
    BOOK.append(ZNAK)
    print("\n")

# variable to check if there will be records
flag = 0
info_znak = input("Insert the zodiac sign you are looking for :")
print("\n")

# new list that will have all the data we need
f_result = []
for i in range(0,len(BOOK)):
    if(info_znak == BOOK[i]["ZODIAC"]):
        f_result.append(BOOK[i])

# sort list using sorted() function
f_result = sorted(f_result, key=lambda d: d['BDAY'])

# show information to the screen
for i in range(0, len(f_result)):
        print("Name Surname : {}".format(f_result[i]["NAME"]))
        print("Zodiac Sign : {}".format(f_result[i]["ZODIAC"]))
        print("Date of birth : {}.{}.{}".format(f_result[i]["BDAY"][2],f_result[i]["BDAY"][1],f_result[i]["BDAY"][0]))
        print("\n")
        flag = 1

# if flag remain 0 that mean there is no record with the type of zodiac sign that we inserted
if(flag == 0) :
    print("There is no person with such zodiac sign!")
