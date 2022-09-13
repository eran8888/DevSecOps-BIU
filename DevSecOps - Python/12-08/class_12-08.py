# Build phone application that turning on or off and also dials a number if it's longer than 9
'''
class phone:
    def turn_on(self):
        print('turning on')

    def turn_off(self):
        print('turning off')

    def dial(self, phone_number):
        # if len(phone_number) >= 9
        # return true
        # else return false
        # but it is easier like this:
        return len(phone_number) >= 9

phone_app = phone()

phone_app.turn_on()

print(phone_app.dial('0542455860'))

'''

# build a function name point that receives x and y as int and color as str and uses init for the vars and str
# to print the results of x and y

class Point:
    # Data
    def __init__(self, x , y, color):
        self.x = x
        self.y = y
        self.color = color
    def __str__(self):
        return f'Point({self.x}.{self.y})'
    def move(self):
        self.x += 1
        self.y += 1

p1 = Point(2,1,'red')
p2 = Point(2,1,'green')

print(p1)

p1.move()
p1.move()

print(p1)









