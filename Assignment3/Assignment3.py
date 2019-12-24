import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import copy as cp
import re
import collections, numpy


def readFile(rawfile):

    text_file = open(rawfile, "r")
    line = text_file.readline()
    lines = []
    while line:
        lines.append(line.replace('"', '').replace("\n", '').split(','))
        line = text_file.readline()
    dataset = np.asarray(lines).astype(float)
    return dataset

def histeq(img):

    unique, count = np.unique(img, return_counts=True)
    totalval = sum(count)
    occ = 0
    cdf = []

    for i in range(len(unique)):
        occ += count[i]
        cdfval = (occ * 255) / totalval
        cdf.append(cdfval)


    for m in range(500):
        for n in range(500):
            ran = np.where(unique == img[m][n])  # Used this function np.where from stackoverflow to reduce computation time
            if ran[0]:
                for k in ran[0]:
                    img[m][n] = cdf[k]


    return img

def main():

    f, axarr = plt.subplots(2, 2)  # Took this subplot function from stackoverflow
    image1 = readFile("i170b1h0_t0.txt")
    image2 = readFile("i170b2h0_t0.txt")
    image3 = readFile("i170b3h0_t0.txt")
    image4 = readFile("i170b4h0_t0.txt")

    plt.figure()
    axarr[0, 0].imshow(image1, cmap='gray', origin='lower')
    axarr[0, 1].imshow(image2, cmap='gray', origin='lower')
    axarr[1, 0].imshow(image3, cmap='gray', origin='lower')
    axarr[1, 1].imshow(image4, cmap='gray', origin='lower')
    plt.show()

    # Task (a), Calculating Max, Min, Mean and Variance
    print("Max Value of the 2D dataset is: ", image2.max())
    print("Min Value of the 2D dataset is: ", image2.min())
    print("Variance Value of the 2D dataset is: ", image2.var())
    print("Mean Value of the 2D dataset is: ", image2.mean())

    # Task (b), Drawing a profile line through line 256
    profLine = np.where(image2 == image2.max())
    print(profLine)

    plt.figure()
    plt.plot(image2[432])
    plt.title('Profile line for max Data')
    plt.show()

    # Task (c), Displaying Histogram of the 2D Data Set
    plt.figure()
    plt.hist(image2, bins='auto')
    plt.title('Histogram of the 2D Data')
    plt.show()


    # Task (c), Displaying Linegraph of the 2D Data Set
    plt.figure()
    LineData, Edge = np.histogram(image2, bins=50)
    Center = 0.75 * (Edge[1:]+Edge[:-1])
    plt.plot(Center, LineData)
    plt.title('Line Graph of The 2D Data')
    plt.show()


    # Task (d) Non-Linear Transformations
    taskd = cp.deepcopy(image2)

    for di in range(0, 500):
        for dj in range(0, 500):
            taskd[di][dj] = math.log2(taskd[di][dj])  # Non-Linear Transformation
            if taskd[di][dj] < 0:
                taskd[di][dj] = 0
            elif taskd[di][dj] > 255:
                taskd[di][dj] = 255

    plt.figure()
    plt.imshow(taskd, cmap='gray', origin='lower')
    plt.title('Non-Linear Transformation')
    plt.show()

    # Task (e) Histogram Equalization
    print("Starting first file")
    eqlImg1 = histeq(image1)
    print("Starting second file")
    eqlImg2 = histeq(image2)
    print("Starting third file")
    eqlImg3 = histeq(image3)
    print("Starting fourth file")
    eqlImg4 = histeq(image4)

    f, arr = plt.subplots(2, 2)  # Took this subplot function from stackoverflow
    plt.figure()
    arr[0, 0].imshow(eqlImg1, cmap='gray', origin='lower')
    arr[0, 1].imshow(eqlImg2, cmap='gray', origin='lower')
    arr[1, 0].imshow(eqlImg3, cmap='gray', origin='lower')
    arr[1, 1].imshow(eqlImg4, cmap='gray', origin='lower')
    plt.show()

    # Task (f) Combining histogram equalized data to form an RGB Image
    final = []

    for o in range(0, 500):
        for p in range(0, 500):
            final.append(int(eqlImg4[o][p]))
            final.append(int(eqlImg3[o][p]))
            final.append(int(eqlImg1[o][p]))

    rgbarray = np.reshape(final, (500, 500, 3))
    plt.figure()
    plt.imshow(rgbarray, origin='lower')
    plt.title("RGB Image")
    plt.show()




if __name__ == "__main__":
    main()
