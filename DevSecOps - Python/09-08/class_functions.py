# write a python function that receives 3 numbers x, y, z and return the biggest number
# if the user sends 2 numbers define the 3rd as "0"
# etgar if the 3rd number wasn't defined do not return it even if it's the greatest

'''
def biggest_number(numb1, numb2, numb3 = 0):
    if numb1 > numb2 and numb1 > numb3:
        return numb1
    elif numb2 > numb3:
         return numb2
    else:
        return numb3

print(biggest_number(-1,-2,-3))

# See answer for etgar in the hodi's github

'''


# write a function that receives unknown numbers and returns the biggest
'''
def my_max(*args):
    print(args)
    big = args[0]
    
    for i in args:
        if big < i:
            big = i
    return big

my_max(1,5,2,7,-2)

# or

def my_max(*args):
    print(sorted(args))
    return sorted(args)[-1]

biggest = my_max(1,5,2,7,-2)

print(biggest)

'''



