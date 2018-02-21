formatter = "%r,%r,%r,%r"

print(formatter %(1,2,3,4))
print(formatter %('one','two','three','four'))
print(formatter %(True,False,True,False))
print(formatter %(formatter,formatter,formatter,formatter))
print( formatter\
       %(
       '我跟你讲讲猫咪有多可爱',
       '有这---------->么可爱',
       '特别可爱',
       '不骗你'
       )
)