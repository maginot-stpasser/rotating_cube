import matplotlib.pyplot as plt

# # 2d rotation test ground
# def twoDRotation(arr, d):
#     theta = np.radians(d)
#     rotationM = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
#     d = np.round(rotationM @ arr, 5)
#     return d 

# vector1 = np.array([[0], [50]])
# changeInDegree = 6

# plt.ion()

# fig, ax = plt.subplots(1, 1)

# q = ax.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1)
# ax.set_aspect('equal', adjustable='box') 
# plt.xlim(-50, 50)
# plt.ylim(-50, 50)
# plt.show()

# for i in range(100):
# # while True:
#     vector1 = twoDRotation(vector1, changeInDegree)
#     q.set_UVC(vector1[0], vector1[1])
#     plt.draw()
#     plt.pause(0.0167)
    
# plt.ioff()
# plt.show()

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


def matPlotCubeInstance(dict_temp, ax = plt.subplot()):
    colourSet = {0:'grey', 1:'red', 2:'green', 3:'blue', 4:'black', 5:'#FF5733'}


    ax.set_aspect('equal', adjustable='box') 
    for key in dict_temp.keys():
        a = dict_temp[key]
        # 1. Define your X and Y coordinate points
        x = a[0, :]
        z = a[2, :]

        # 2. Plot individual points using 'o' (circle marker)
        # Note: 'ro' makes them red circles, 'bo' makes them blue, etc.
        ax.plot(x, z, 'o', color=colourSet[key])
        plt.title("Plotting Points in Python")
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        

