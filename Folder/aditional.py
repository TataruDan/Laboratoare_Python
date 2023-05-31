# Problem nr. 16

number = int(input("Insert a number : "))

for i in range(1, number+1):
    s = 0
    j = i
    while j != 0:
        s = s + int(j % 10)
        j = j / 10
    if i % s == 0 or s % i == 0:
        print(i,end=" ")

# Problem nr. 19
print("\n\n")
i = 10
while(i <= 99):
    c = i // 15
    if(i % 15 == c * c):
        print(i)
    i += 1