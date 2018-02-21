a = 23
b = True
while b:
    try:
        c = int(input('Enter a num:'))
    except ValueError as e:
        print('Pls enter a number')
        continue
    print('c =',c)

    if a==c:
        print('Bingo')
        b = False
        #break
    elif a<c:
        print('Higher')
        #continue
    else:
        print('Lower')
        #continue

else:
    print('Exit')