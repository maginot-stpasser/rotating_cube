import numpy as np;
import tkinter as tk
import time
import math

import matplotlib.pyplot as plt

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
vertex1 = np.array([50, 50])





arr = np.full((3,3,3), 1);
print(arr[0,0])


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.margins(100) 

X, Y, Z = np.full((3), 0)
ax.quiver(X, Y, Z, arr[0, 0], [2,5,1], [1,-11,1])
plt.show()


# # TK config
# root = tk.Tk();
# root.title("Rotation Visualization");
# root.geometry("1366x768")
# text_box = tk.Text(root, font=("Helvetica", 12), bg="black", fg="#00bfff");
# text_box.tag_configure("center", justify='center')
# text_box.insert("1.0", "Hello in the middle!", "center")
# text_box.pack(expand=True, fill=tk.BOTH);
# def update_box():
#     i = time.time()
#     text_box.config(state=tk.NORMAL)   # Enable editing to change text
#     text_box.delete("1.0", tk.END)    # Clear from position 1 (i.e., 0) to the end
#     text_box.insert(tk.END, '\n\n')
#     text_box.insert(tk.END, arr, "center") # Insert new text
#     text_box.config(state=tk.DISABLED) # Disable editing again
#     root.after(1000, update_box)
# update_box()
# root.mainloop()


# for i in range(3):
#     tk
# print(arr, end="\r")
# print(arr, end="\r")
# print(arr, end="\r")
# print(arr, end="\r")
