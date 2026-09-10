import numpy as np;
import tkinter as tk
import time
import math

import matplotlib.pyplot as plt
import opensimplex
import Testing as tt
import os

os.system("")
first_frame = True

# Experimenting on a vertex in 2d
# suppose there is a vertex [5*sqrt(2),5*sqrt(2)] ### ,*5sqrt(2)

#    / ‾ ‾ ‾ \
#  /           \
# | | ‾ ‾ ‾ ‾ | | 
# | |         | |
# | |         | |
#  \ ‾ ‾ ‾ ‾ ‾ /
#    \ _ _ _ /
 
 # _
 # 50
 # 50
 # _



def threeDRotate(arr, a, b, c):
    sinA, cosA = np.sin(a), np.cos(a)
    sinB, cosB = np.sin(b), np.cos(b)
    sinC, cosC = np.sin(c), np.cos(c)
    temp_arr = np.array([[(cosA * cosC - sinA * sinB * sinC), -(sinA * cosB), (cosA * sinC + sinA * sinB * cosC)], 
                         [(sinA * cosC + cosA * sinB * sinC), (cosA * cosB), (sinA * sinC - cosA * sinB * cosC)], 
                         [-(cosB * sinC), (sinB), (cosB * cosC)]])
    return temp_arr @ arr

# def currentAngleContoller(t):
#     x = 0.1 * np.sin(t)
#     y = 0.2 * np.sin(t)
#     z = 0.3 * np.sin(t)
#     return [x, y, z]

def smoothRandomController(t, seed=0): # Todo: smootthen the rotation, and it is awkward
    # Initialize the generator with an integer seed
    tmp_noise = opensimplex.OpenSimplex(seed=int(seed))
    
    # noise2d evaluates smooth noise at a 2D coordinate (time, offset)
    x = tmp_noise.noise2(t * 0.5, 0) * math.pi
    y = tmp_noise.noise2(t * 0.5, 10) * math.pi
    z = tmp_noise.noise2(t * 0.5, 20) * math.pi
    
    return [x, y, z]

def getVertices(arr):
    def dotDegree(arr, iniV = [0, 5, 0]):
        mag_a = np.linalg.norm(arr)
        mag_b = np.linalg.norm(iniV)
        ang = np.arccos(np.dot(arr, iniV) / (mag_a * mag_b))
        if ang >= math.pi/2:
            return False
        else:
            return True
    faceInd = []
    res = {}
    for i in range(3):  
        # only three faces will be shown at the same time when fixed 3d view point
        # find the faces to be shown, and get them indexed for the specific symbols
        if dotDegree(arr[:,i]):
            faceInd.append(2*i)
        else:
            arr[:,i] = -arr[:,i]
            faceInd.append(2*i+1)
    for i in range(3): # find the four vertex vectors representing the vertexes of the particular face
        vertVecs = np.empty((3,1))
        a = arr[:,i: i+1]
        b = arr[:,(i+1) % 3: (i+1) % 3 + 1]
        c = arr[:,(i+2) % 3: (i+2) % 3 + 1]
        vertVecs = np.concatenate((vertVecs, a+b+c), axis=1) # to ensure the 
        vertVecs = np.concatenate((vertVecs, a+b-c), axis=1)
        vertVecs = np.concatenate((vertVecs, a-b-c), axis=1)
        vertVecs = np.concatenate((vertVecs, a-b+c), axis=1)
        # print(vertVecs)
        # print(vertVecs.shape)
        res[faceInd[i]] = vertVecs[:, 1:]
    return res

def printPolygon(dictIn):
    def render(temp_arr):
        global first_frame
        output = "\n".join("".join(row) for row in temp_arr)
        if not first_frame:
            # Move cursor up GRID_SIZE lines, back to the top of the grid
            print(f"\033[{GRID_SIZE}A", end="")
        print(output)
        first_frame = False

    def checkLeftRightOn(arr, point):
        left = []
        for i in range(4):
            # cross product between edge and point vector with from the same starting point, a[0] * b[1] - a[1] * b[0]
            edgeVec = arr[:, [i]] - arr[:, [(i + 1) % 4]]
            pointVec = point - arr[:, [(i + 1) % 4]]
            if (edgeVec[0] * pointVec[1] - edgeVec[1] * pointVec[0]) >= 0:
                left.append(True)
            else:
                left.append(False)
        if np.sum(left) == 4 or  np.sum(left) == 0:
            return True
        else:
            return False

    GRID_SIZE = 30
    half_GRID_SIZE = int(GRID_SIZE/2)
    symbolSet = {0: '+', 1:'-', 2: '#', 3: '@', 4: '*', 5: '~'}
    temp_arr = np.full((GRID_SIZE, GRID_SIZE), '.')
    for key in dictIn.keys():   # Todo: brute
        dictIn[key] = np.delete(dictIn[key], 1, axis=0) # from three d to two d, popping the y coor
        for i in range(int(-(len(temp_arr)/2)), int(((len(temp_arr)/2)))): 
            for j in range(int(-(len(temp_arr)/2)), int(((len(temp_arr)/2)))):
                if checkLeftRightOn(dictIn[key], np.array([[i], [j]]).reshape(2,1)):
                    temp_arr[i+half_GRID_SIZE][j+half_GRID_SIZE] = symbolSet[key]
    render(temp_arr)

height, width = 100, 100

def __main__():
    # Z upward, Y out of the paper
    cubeSide = 8
    vecArr = [[cubeSide, 0, 0],
        [0, cubeSide, 0],
        [0, 0, cubeSide]]


    for t in range(180):

        angles = smoothRandomController(t)
        vecArr = threeDRotate(vecArr, angles[0], angles[1], angles[2])
        VertexVecs = getVertices(vecArr) # {1: [array([0.01449601, 5.33953401, 4.63564089]), array([-6.93831105,  0.90474558, -1.02042891]), array([-2.49763847,  6.33701242, -1.89844031]), array([-4.42617657, -0.09273283,  5.51365229])], ...}
        # if t == 170:
        #     tt.matPlotCubeInstance(VertexVecs)
        #     plt.show()
        
        printPolygon(VertexVecs)
        # print(VertexVecs)
        time.sleep(0.1)
    
        
__main__()

# from skimage.draw import polygon
# import numpy as np

# # Coordinates (x, y)
# coords = np.array([[5, 1], [9, 5], [5, 9], [1, 5]])

# grid = np.full((12, 12), " ")

# # skimage uses (row, column) which maps perfectly to (y, x)
# rr, cc = polygon(coords[:, 1], coords[:, 0])
# grid[rr, cc] = "#"

# print("\n".join("".join(row) for row in grid))





# # matplotlib
# vector1 = np.array([[10], [10], [0]])
# vector1_ori = np.array([[10], [-10], [0]])

# plt.ion()

# # fig, ax = plt.subplots(1, 1)
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# # q = ax.quiver(0, 0, 0, vector1[0], vector1[1], vector1[2])
# ax.set_aspect('equal', adjustable='box') 
# ax.set_xlim(-50, 50)
# ax.set_ylim(-50, 50)
# ax.set_zlim(-50, 50)
# plt.show()

# for i in range(720):
# # while True:
#     q = ax.quiver(vector1_ori[0], vector1_ori[1], vector1_ori[2], vector1[0], vector1[1], vector1[2])
#     currAng = currentAngle(i)
#     vector1 = fullRotateED(vector1, currAng[0], currAng[1], currAng[2])
#     vector1_ori = fullRotateED(vector1_ori, currAng[0], currAng[1], currAng[2])
#     # q.set_UVC(vector1[0], vector1[1], vector1[2])
#     plt.draw()
#     plt.pause(0.01)
#     q.remove()
    
# plt.ioff()
# plt.show()

