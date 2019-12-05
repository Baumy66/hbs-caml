import math

# Variables & Mathematics
x = 1000
#print(x)
y = 1000/555
#print(y)
z = 10 % 7
#print(z)

# Functions
def pythagoreanHypotenuse(a, b):
    t = a*a + b*b
    c = math.sqrt(t)
    return c

# Hypotenuse should equal 5
hypotenuse = pythagoreanHypotenuse(3,4)
# print(hypotenuse)

# Hypotenuse should equal 13
biggerHypotenuse = pythagoreanHypotenuse(5,12)
# print(biggerHypotenuse)


# Conditions
def isItRight(a,b,c):
    hypotenuseForRightTriangle = pythagoreanHypotenuse(a,b)
    if(float(c) == hypotenuseForRightTriangle):
        return True
    else:
        return False

def printMessage(a,b,c,right):
    if(right):
        confirmation = ''
    else:
        confirmation = 'NOT '
    message = 'A ' + str(a) + ', ' + str(b) + ', ' + str(c) + ' triangle is ' + confirmation + 'a right triangle.'
    print(message)

is456TriangleRight = isItRight(3,4,5)
is567TriangleRight = isItRight(5,6,7)

#printMessage(3, 4, 5, is456TriangleRight)
#printMessage(5, 6, 7, is567TriangleRight)

# Loops
upperLimit = 300
numberOfRight = 0
a=0
while(a<upperLimit):
    b=0
    while(b<upperLimit):
        c = 0
        while(c<upperLimit):
            isRight = isItRight(a,b,c)
            if(isRight and a != 0 and b != 0 and c != 0):
                # printMessage(a, b, c, isRight)
                numberOfRight = numberOfRight + 1
            c = c + 1
        b = b + 1
    a = a + 1
    if(a % 100 == 0):
        print(a)

print('The number of right triangles below ' + str(upperLimit) + ' is ' + str(numberOfRight))