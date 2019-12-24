import numpy as np
from matplotlib import pyplot as plt
import math
import copy

A = np.fromfile('slice150.raw', dtype='uint16', sep="")

B = np.reshape(A, (512, 512))

print('test')

plt.figure()
plt.imshow(B, cmap='gray', origin='lower')
plt.title('Original Image')
plt.colorbar(orientation='vertical')
plt.show()


#Task (a), Drawing a profile line through line 256
plt.figure()
plt.plot(B[255])
plt.title('Profile line for Data Line 256')
plt.show()


#Task (b), Calculating Mean and Variance
print("Mean: ", B.mean())
print("Variance: ", B.var())


#Task (c), Displaying Histogram of the 2D Data Set
plt.figure()
plt.hist(B, histtype='stepfilled')
plt.title('Histogram of the 2D Data')
plt.show()


#Task (c), Displaying Linegraph of the 2D Data Set
plt.figure()
Data, Edge = np.histogram(B, bins=150)
Center = 0.50 * (Edge[1:]+Edge[:-1])
plt.plot(Center, Data)
plt.title('Line Graph of The 2D Data')
plt.show()


#Task (d) & (e), Linear and Non-Linear Transformations
taskd = copy.deepcopy(B)
taske = copy.deepcopy(B)
di = 0
dj = 0

for di in range(512):
    for dj in range(512):
        taskd[di][dj] = (taskd[di][dj] * 0.5) #Linear Transformation
        taske[di][dj] = math.log2(math.sqrt(taske[di][dj])+1)  # Non-Linear Transformation
        if taskd[di][dj] > 255:
            taskd[di][dj] = 255
        elif taskd[di][dj] < 0:
            taskd[di][dj] = 0


plt.figure()
plt.imshow(taskd, cmap ='gray', origin='lower')
plt.title('Linear Transformation')
plt.show()

plt.figure()
plt.imshow(taske, cmap='gray', origin='lower')
plt.title('Non-Linear Transformation')
plt.show()


#Used online sources such as Stackoverflow to take help in implementing some of the logics used in the work below
#Task (f), Applying Boxcar smoothing filter
taskf = np.ones((11, 11), dtype=np.uint16)
temp1 = copy.deepcopy(B)

count = 0
l = 0
k = 0

for l in range(11):
    for k in range(11):
        count += taskf[l][k]


fi = 0
fj = 0
boxsum = 0

for fi in range(501):
    for fj in range(501):
        boxsum = sum(sum(temp1[fi: fi+11, fj: fj+11]))
        temp1[fi+5][fj+5] = boxsum / count


plt.figure()
plt.imshow(temp1, cmap='gray', origin='lower')
plt.title('Boxcar Smoothing Filter')
plt.show()



#Task (g), Applying Median Filter
temp2 = copy.deepcopy(B)
gi = 0
gj = 0
for gi in range(501):
    for gj in range(501):
        flatdata = (temp2[gi: gi+11, gj: gj+11]).flatten('C')
        sortdata = np.sort(flatdata)
        temp2[gi+5][gj+5] = sortdata[int(len(sortdata)/2)]


plt.figure()
plt.imshow(temp2, cmap='gray', origin='lower')
plt.title('Median Filter')
plt.show()

