n = 109
str_1= str(n)

while n !=1:
    if n % 2 == 1:
        n = 3*n + 1
    else:
        n = int(n/2)
    if n < 255:
        str_1+= ' ' + str(n)

print(str_1)
