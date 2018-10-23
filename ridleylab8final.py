'''
Program: vector.py
Author: Elayna Ridley
Purpose: Using a list of vectors input by the user, print them, get their dimension, add them,
compute the dot product and magnitude, compare magnitudes, and get the maximum value.
Input: Vectors
Output: List of vectors, vector dimensions, dot product, magnitude, magnitude comparison,
and maximum value.

'''

########### import statements ##########

import math

########### functions #########

def maxBoth(v1, v2):
    v3 = v1 + v2
    max = v3[0]
    for i in range(len(v3)):
        if v3[i] > max:
            max = v3[i]
    print(max)
    return max
    

def compareMagnitudes(v1, v2):
    m1, m2 = magnitude(v1, v2)
    if m1 > m2:
        print('The magnitude of v1 (', m1, ') is larger than the magnitude of v2 (', m2, ')')
    elif m1 < m2:
        print('The magnitude of v1 (', m1, ') is smaller than the magnitude of v2 (', m2, ')')
    else:
        print('The magnitude of v1 (', m1, ') is equal to the magnitude of v2 (', m2, ')')


def printMagnitudes(m1, m2):
    print('The magnitude of v1 is', m1)
    print('The magnitude of v2 is', m2)
    

def magnitude(v1, v2):
    sqlist1 = []
    sqlist2 = []
    for i in range(len(v1)):
        sq1 = v1[i] ** 2
        sqlist1.append(sq1)
        sq1sum = sum(sqlist1)
        m1 = math.sqrt(sq1sum)
        sq2= v2[i] ** 2
        sqlist2.append(sq2)
        sq2sum = sum(sqlist2)
        m2 = math.sqrt(sq2sum)
    return m1, m2
    

def dotProduct(v1, v2):
    multlist = []
    addmultlist = []
    for i in range(len(v1)):
        mult = v1[i] * v2[i]
        multlist.append(mult)
    addmult = sum(multlist)
    
    print('The dot product of v1 and v2 is', addmult)

def addVectors(v1, v2):
    addlist = []
    for i in range(len(v1)):
        add = v1[i] + v2[i]
        addlist.append(add)
    print('The sum of the vectors is', addlist)

def vecDim(v1, v2):
    print('The dimensionality of the vectors is', len(v1))

def printVectors(v1, v2):
    print('v1:', v1)
    print('v2:', v2)

def getVectors():
    vec1 = []
    vec2 = []
    print('Type a value <= -1000 when done')
    vec1val = float(input('Enter first vector values: '))
    while not vec1val <= -1000:
        vec1.append(vec1val)
        vec1val = float(input('Enter first vector values: '))
    for i in range(len(vec1)):
        vec2val = float(input('Enter second vector values: '))
        vec2.append(vec2val)
    return vec1, vec2


def main():
    v1 = []
    v2 = []
    print('Welcome to vector arithmetic! Below is a list of available operations.')
    print('1. Enter values for your vectors ')
    print('2. Print vectors')
    print('3. Vector dimensionality')
    print('4. Add vectors')
    print('5. Compute dot product of vectors')
    print('6. Compute magnitude of vectors')
    print('7. Compare magnitudes of vectors')
    print('8. Print magnitudes of vectors')
    print('9. Get maximum value from both vectors')
    print('10. Quit')
    print()

    while True:
        command = input('Enter the number corresponding to your choice: ')
        
        if command == '1':
            v1, v2 = getVectors()
        elif command == '2':
            printVectors(v1, v2)
        elif command == '3':
            vecDim(v1, v2)
        elif command == '4':
            addVectors(v1, v2)
        elif command == '5':
            dotProduct(v1, v2)
        elif command == '6':
            m1, m2 = magnitude(v1, v2)
        elif command == '7':
            compareMagnitudes(v1, v2)
        elif command == '8':
            printMagnitudes(m1, m2)
        elif command == '9':
            maxBoth(v1, v2)
        elif command == '10':
            break
        
########### main program ######

main()
