# EX1:
# x=3
# print 1,1,1,2,2,3
'''
x = 3
i = 1

while i < 4:
    for j in range(x):
        print (i, end = ',')
    i += 1
    x -= 1
'''


# EX12 (hw208.pdf)

import random
randomlist = []
newlist = []
for i in range(0,5):
    n = random.randint(2,49)
    randomlist.append(n)

print(randomlist)

counter = 0

while True:
    number = int(input('Enter Number: '))
    if (number < 2) and (number > 49):
        continue

    counter += 1

    #Etgar1 - If user guessed the same number twice - break

    if number in newlist:
        print('You guessed the same number twice')
        break
    else:
        newlist.append(number)

    if number in randomlist:
        randomlist.remove(number)
        print(randomlist)
        print(newlist)

        if len(randomlist) == 0:
            print(f'You Won! it took you {counter} times')
            break
        else:
            continue











