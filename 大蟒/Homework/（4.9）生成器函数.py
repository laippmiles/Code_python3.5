def get_odds():
    for num in range(0,10):
        if num % 2 ==1:
            yield num

for num in get_odds():
    print(num)