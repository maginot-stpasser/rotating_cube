import numpy as np;
import time

# import matplotlib.pyplot as plt
import math
# import opensimplex
# from skimage.draw import polygon

# import os

import Testing as tt

# os.system("")
first_frame = True

def threeDRotate(arr, a, b, c):
    # given the vectors and angles of rotation, rotate using z, x, y as axises
    sinA, cosA = np.sin(a), np.cos(a) # looking at xy plane
    sinB, cosB = np.sin(b), np.cos(b) # looking at yz plane
    sinC, cosC = np.sin(c), np.cos(c) # looking at zx plane
    temp_arr = np.array([[(cosA * cosC - sinA * sinB * sinC), -(sinA * cosB), (cosA * sinC + sinA * sinB * cosC)], 
                         [(sinA * cosC + cosA * sinB * sinC), (cosA * cosB), (sinA * sinC - cosA * sinB * cosC)], 
                         [-(cosB * sinC), (sinB), (cosB * cosC)]])
    return temp_arr @ arr

def smoothRandomController(t, tmp_noise=0): # Todo: smootthen the rotation, and it is awkward
    # Initialize the generator with an integer seed
    
    # noise2d evaluates smooth noise at a 2D coordinate (time, offset)
    # x = np.sin(tmp_noise.noise2(t * 0.5, 0) * 20) / 20 # * np.pi
    # y = np.sin(tmp_noise.noise2(t * 0.5, 10) * 20) # * np.pi
    # z = np.sin(tmp_noise.noise2(t * 0.5, 20) * 20) # * np.pi
    x = 0.02
    y = 0.09
    z = 0.10
    
    return [x, y, z]

def getVertices(arr):
    def dotDegree(arr, iniV = [0, 5, 0]): # find the angle between the y axis and the face vec using arcosing the dot product
        mag_a = np.linalg.norm(arr)
        mag_b = np.linalg.norm(iniV)
        ang = np.arccos(np.dot(arr, iniV) / (mag_a * mag_b))
        if ang < np.pi/2:
            return True
        else:
            return False
    faceInd = []
    res = {}
    for i in range(3):  
        # only three faces will be shown at the same time with fixed 3d view point looking into a 2d plane
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
        vertVecs = np.concatenate((vertVecs, a+b+c), axis=1)
        vertVecs = np.concatenate((vertVecs, a+b-c), axis=1)
        vertVecs = np.concatenate((vertVecs, a-b-c), axis=1)
        vertVecs = np.concatenate((vertVecs, a-b+c), axis=1)
        # print(vertVecs)
        # print(vertVecs.shape)
        res[faceInd[i]] = vertVecs[:, 1:]
    return res

def printPolygon(dictIn, GRID_SIZE=30):
    dict_temp = dictIn.copy()
    def render(temp_arr):
        global first_frame
        output = "\n".join("".join(row) for row in temp_arr)
        if not first_frame:
            # Move cursor up GRID_SIZE lines, back to the top of the grid
            print(f"\033[{GRID_SIZE}A", end="")
            # print("\033[H", end="")
            # print("\033[2J", end="")
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
        if np.sum(left) == 4 or np.sum(left) == 0:
            return True
        else:
            return False

    half_GRID_SIZE = int(GRID_SIZE/2)
    symbolSet = {0: '+', 1:'=', 2: '#', 3: '@', 4: '*', 5: '~'}
    grid = np.full((GRID_SIZE, GRID_SIZE), '.')
    sorted_data = dict(sorted(dict_temp.items(), key=lambda item: np.max(item[1][1, :]) - np.min(item[1][1, :])))
    for key in sorted_data.keys():
        dict_temp[key] = np.delete(dict_temp[key], 1, axis=0) # from three d to two d, popping the y coor

        # # Use skimage for finding the vertices coordinates
        # rr, cc = polygon(dict_temp[key][:, 1].astype(int) + half_GRID_SIZE, dict_temp[key][:, 0].astype(int) + half_GRID_SIZE)
        # temp_arr[rr, cc] = symbolSet[key]

        # shrink the size to rectangles to be searched
        max_x, min_x = math.ceil(np.max(dict_temp[key][0, :])), math.ceil(np.min(dict_temp[key][0, :]))
        max_z, min_z = math.ceil(np.max(dict_temp[key][1, :])), math.ceil(np.min(dict_temp[key][1, :]))
        # Search
        for i in range(min_x, max_x):
            for j in range(min_z, max_z):
                if checkLeftRightOn(dict_temp[key], np.array([[i], [j]]).reshape(2,1)):
                    grid[j+half_GRID_SIZE][i+half_GRID_SIZE] = symbolSet[key]

        # Todo: brute
        # for i in range(int(-(len(temp_arr)/2)), int(((len(temp_arr)/2)))): 
        #     for j in range(int(-(len(temp_arr)/2)), int(((len(temp_arr)/2)))):
        #         if checkLeftRightOn(dict_temp[key], np.array([[i], [j]]).reshape(2,1)):
        #             temp_arr[j+half_GRID_SIZE][i+half_GRID_SIZE] = symbolSet[key]

    render(grid)

def main():
    # let Z upward, Y out of the paper
    cubeSide = 6
    GRID_SIZE = cubeSide * 5
    vecArr = [[cubeSide, 0, 0], # X
        [0, cubeSide, 0],       # Y
        [0, 0, cubeSide]]       # Z
    t = 0
    while True:
        t += 1
        # temp_noise = opensimplex.OpenSimplex(seed=int(0))
        temp_noice = 0
        angles = smoothRandomController(t, temp_noice)
        vecArr = threeDRotate(vecArr, angles[2], angles[0], angles[1])
        VertexVecs = getVertices(vecArr) # {1: [array([0.01449601, 5.33953401, 4.63564089]), array([-6.93831105,  0.90474558, -1.02042891]), array([-2.49763847,  6.33701242, -1.89844031]), array([-4.42617657, -0.09273283,  5.51365229])], ...}
        printPolygon(VertexVecs, GRID_SIZE)

        # if t == 20:
        #     tt.matPlotCubeInstance(VertexVecs)
        #     plt.show()

        time.sleep(1/25) # 25 fps
        
if __name__ == '__main__':
    main()
