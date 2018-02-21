#疑似取余法
B = '1101'
I = 0
print('B = ',B)
print("ord('0') = ",ord('0'))
i = 1
while B != '':
    print('-'*10,'第',i,'轮转换','-'*10)
    print('B[0] = ', B[0])
    print('ord(B[0]) = ',ord(B[0]))
    I = I * 2 + (ord(B[0]) - ord('0'))
    print("(ord(B[0]) - ord('0')) = ",(ord(B[0]) - ord('0')))
    print('I = ',I)
    B = B[1:]
    if B == '':
        print("Over")
    else:
        print('B = ',B)
    i = i + 1