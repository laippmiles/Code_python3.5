def cheese_and_cracker(cheese_count,boxes_of_crackers):
    print("You have %d cheeses!"%cheese_count)
    print("You have %d boxes of crackers!"%boxes_of_crackers)
    print("Man that is enough of a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_cracker(20,30)

print("Or,we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_cracker(amount_of_cheese,amount_of_crackers)

print("We can even do math inside too.")
cheese_and_cracker(10+5,2**2)

print("We can combine two,variables and math:")
cheese_and_cracker(amount_of_cheese+10,amount_of_crackers-2)