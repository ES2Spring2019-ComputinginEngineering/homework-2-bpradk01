# HOMEWORK 2 --- ES2
# Triangle Calculator

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Ben Pradko
# NUMBER OF HOURS TO COMPLETE: 1.5 Hrs (please track how long this homework takes you to complete).
# YOUR COLLABORATION STATEMENT(s) (refer to syllabus):
#
#*****************************************

#In this homework,the ultimate goal is to create a function called areaofatriangle,
#which takes six parameters which represent three intersecting lines
#of the form y = (m * x) + b that mark the three sides of the triangle.

#In order to accomplish this you will need functions which determine
#where two lines intersect (x and y), a function which determines the distance between
#two points represented by (x,y) coordinates, and a function which determines
#the area of a triangle using three side lengths(using Heron's Formula).

#Please complete the four required functions below:

import math  #This line allows you to use math functions. Importantly, math.sqrt(#) which will produce the square root of the number inside the parentheses.


def intersectionoftwolines_x(m1, b1, m2, b2):
    # Calculate x for the point where two equations:
    # y = (m1 * x) + b1 and y = (m2 * x) + b2 intersect.
    #b1-b2=(m2*x)-(m1*x)
    #b1-b2=x(m2-m1)
    x = ((b1-b2)/(m2-m1))
    return x

def intersectionoftwolines_y(m1, b1, m2, b2):
    # Calculate y for the point where two equations:
    # y = (m1 * x) + b1 and y = (m2 * x) + b2 intersect.
    #x=((y-b)/m)
    #((y-b1)/m1)=((y-b2)/m2)
    #m2(y-b1)=m1(y-b2)
    #m2*y-m2*b1=m1*y-m1*b2
    #m2*y-m1*y=m2*b1-m1*b2
    #y(m2-m1)=(m2*b1-m1*b2)
    #y=(m2*b1-m1*b2)/(m2-m1)
    y = ((m2*b1-m1*b2)/(m2-m1))
    return y

def distancebetweenpoints(x1, y1, x2, y2):
    # Calculate the linear distance between two points
    # (x1, y1) and (x2, y2).
    #distance equation is sqrt of (x2-x1)**2+(y2-y1)**2

    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance

def heronsformula(a, b, c):
    # Calculate the area of a triangle with three known side lengths.
    # You may want to look up Heron's formula online.
    #herons formula sqrt (s(s-a)(s-b)(s-c))
    #s=(a+b+c)/2

    s = ((a+b+c)/2)
    area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    return area

def areaofatriangle(m1, b1, m2, b2, m3, b3):
    #Using the three functions above, now calculate the area of a
    #triangle when the three sides are described by three linear equations
    #y = (m1 * x) + b1;  y = (m2 * x) + b2; and y = (m3 * x) + b3

    #x intersection points
    x1 = ((b1-b2)/(m2-m1))
    x2 = ((b2-b3)/(m3-m2))
    x3 = ((b3-b1)/(m1-m3))
    #y intsection points
    y1 = ((m2*b1-m1*b2)/(m2-m1))
    y2 = ((m3*b2-m2*b3)/(m3-m2))
    y3 = ((m1*b3-m3*b1)/(m1-m3))
    #side lengths
    s1 = math.sqrt((x2-x1)**2+(y2-y1)**2)
    s2 = math.sqrt((x3-x2)**2+(y3-y2)**2)
    s3 = math.sqrt((x1-x3)**2+(y1-y3)**2)
    #Heron's Equation, s value
    s = (((s1)+(s2)+(s3))/2)

    area = math.sqrt((s*(s-(s1))*(s-(s2))*(s-(s3))))
    return area


#TEST CASES
#These print statements will be true when your functions are working.

print("Distance between Points:")
#If these are both true, it is likely that your function is working.
print(distancebetweenpoints(0, 0, 3, 4) == 5)
print(distancebetweenpoints(0, 0, 1, 1) == math.sqrt(2))
print("*********")

print("Intersection of Two Lines:")
#If these are all true, it is likely that your function is working.
print(round(intersectionoftwolines_x(3, -3, 2.3, 4),2) == 10)
print(round(intersectionoftwolines_y(3, -3, 2.3, 4),2) == 27)
print(round(intersectionoftwolines_x(10, 10, 30, 0),2) == .5)
print(round(intersectionoftwolines_y(10, 10, 30, 0),2) == 15)
print("*********")

print("Heron's Formula:")
print(round(heronsformula(5, 5, 8), 2) == 12)
print(round(heronsformula(5, 5, 6), 2) == 12)
print("*********")

print("Area of a Triangle:")
#If these are both true, it is likely that your function is working.
print(round(areaofatriangle(10, 10, 20, 0, 30, 0),2) == 2.5)
print(round(areaofatriangle(0, 0, 1, 0, -1, 10),2) == 25)
print("*********")