'''
x = 12
y = 144

if x == y:
    print ('x equals y')

else:
    print(" x not equals y")

print('after if statement ')
'''

'''
password = input('please enter your password: ')

if password == 'Pa$$w0rd':
    print('Access Granted')

else:
    print('Try again')
'''

word = input('please enter a key word: ')
for guess in range(5):
    guess1=input('enter your guess: ')
    if guess1 == word:
        print('Kol Hakavod!')
        break
    else:
        print("Not good. Try again")