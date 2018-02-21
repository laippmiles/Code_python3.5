n = 2
# n为待转换进制

while True:
    B = input("Input a number:\n")
    FlagBitError = 0
    if not B.isdigit():
        print("Something Input isn't a number , Try Again")
        continue
    for W in B:
        if int(W) >= n :
            print("Something Input higher than bit , Try Again")
            FlagBitError = 1
            break

    if FlagBitError == 1:
        continue

    break

B = B[::-1]
print('B = ',B)
I = 0
i = 0
while B != '':
    I = I +  n ** i * int(B[0])
    print('B[0] = ',B[0])
    print('I = ',I)
    B = B[1:]
    i = i + 1
print(I)