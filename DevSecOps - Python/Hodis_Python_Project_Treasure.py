import random

#Phase 1

name = input('Please enter your name: ')
print(f'Welcome {name} to "Treasure Hunting Game!"')

with open('treasure1.txt', 'w') as file:
    for n in range(0, 10):
        r = random.randint(1, 20)
        for i in range(r):
            # print(n, end='')
            file.write(f'{n}')
        if n == 9:
            # print('TREASURE')
            file.write('TREASURE')
    for n in range(9, -1, -1):
        r = random.randint(1, 20)
        for i in range(r):
            # print(n, end='')
            file.write(f'{n}')


# phase 2
counter = 0

with open('treasure1.txt', 'rb') as file1:
    while True:
        counter += 1
        print(f'\nYou are now in square {file1.tell()} ')
        choice = int((input('\nWhere do you want to move? [1 - Forward, 2 - Backwards]  ')))
        chars = int((input('\nHow many characters?  ')))
        if choice == 1:
            file1.seek(chars, 1)
            data = file1.read(1).decode("utf-8")
            if data in ['T', 'R', 'E', 'A', 'S', 'U']:
                print(f'"{data}" You found the treasure!')
                break
            else:
                print(f'{data}\ntry again! ')
        elif choice == 2 and int(file1.tell()) == 0:
            print ('You must first go forward')
        else:
            file1.seek(-abs(chars), 1)
            data = file1.read(1).decode("utf-8")
            if data in ['T', 'R' , 'E' , 'A' , 'S' , 'U']:
                print(f'"{data}" You found the treasure!')
                break
            else:
                print(f'{data}\ntry again! ')

print(f'It took you {counter} times to find it. Congrats! ')
