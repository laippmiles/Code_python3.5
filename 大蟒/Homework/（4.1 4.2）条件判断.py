import random
guess_me = random.randint(1,14);
start = random.randint(1,14);

if guess_me < 7:
    print(guess_me,'too low');
elif guess_me > 7:
    print(guess_me,'too high');
else:
    print(guess_me,'just right');

while True:
    if start > guess_me:
        print('start:',start,'guess_me',guess_me,'oops!');
        break;
    elif start == guess_me:
        print('start:',start,'guess_me',guess_me,'found it!');
        break;
    else:
        print('start:',start,'guess_me',guess_me,'too low!')
        start = start + 1;
