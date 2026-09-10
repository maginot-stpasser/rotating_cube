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
        
        
        # 4. Display the plot
        # plt.show()

