import collections
import math
import numpy

def init_floor(size = 500):
    floor = []
    for i in range(0,size):
        row = []
        for j in range(0,size):
            row.append(0)
        floor.append(row)
    return floor
   
def printFloor(floor):
    for i in floor:
        for j in i:
            if j == 0:
                print('.',sep='',end='')
            else:
                print(j,sep='',end='')
        print('')

def makePoint(pointStr):
    pointList = pointStr.split(',')
    retval = []
    retval.append(int(pointList[0]))
    retval.append(int(pointList[1]))
    return retval

def updateLine(floor, pointA, pointB, hv_only = True):
    pointA = makePoint(pointA)
    pointB = makePoint(pointB)
    vec = [pointB[0] - pointA[0],pointB[1] - pointA[1]]
    print (pointA, pointB, vec)
    cursor = pointA
    
    if (hv_only and (vec[0] == 0 or vec[1] == 0)) or not hv_only:
        vec[0] = 1 if vec[0] > 0 else 0 
        vec[1] = 1 if vec[1] > 0 else 0 
    
        while cursor != pointB:
            floor[cursor[0]][cursor[1]] += 1
            cursor[0] += vec[0]
            cursor[1] += vec[1]
            print(cursor)
    
    return floor
    

  
def partA(file = "Input/5A.txt"):
    if file == "test":
        file = "Input/5A_test.txt"
    with open(file) as f:
        lines = f.readlines()
        
    floor = init_floor(10)
    printFloor(floor)
    
    for i in lines:
        i = i.split(' ')
        floor = updateLine(floor, i[0], i[2])
        printFloor(floor)
    