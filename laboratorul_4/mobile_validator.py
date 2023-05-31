import re
phone_numbers = ["+373 22345654","+(373) 22 34-56-54","0 0 373 22 345653","0 22 34-56-67","(022) 34567","(022)34-34-56","022 34.45.67"]
for phone in phone_numbers:
    if re.match(r"^[\+\(]?\d+(?:[- \)\(]+\d+)+$", phone) != None:
        print("Valid")
    else:
        print("Invalid")