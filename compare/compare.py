#!/usr/bin/env python

from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def MSE(imgA , imgB):
    #defining the MSE function
    error = np.sum((imgA.astype("float") - imgB.astype("float"))**2)
    error /= float(imgA.shape[0] * imgA.shape[1])

    return error

def compare_images(imgA, imgB):
    #computing mse and ssim separately for two images
    m = MSE(imgA, imgB)
    s = ssim(imgA, imgB)

    #setup the figure
    fig = plt.figure("Comparison")
    plt.suptitle("MSE: %.2f, SSIM: %.2f" %(m,s))

    #show first image
    ax = fig.add_subplot(1,2,1)
    plt.imshow(imgA, cmap = plt.cm.gray)
    plt.axis("off")

    #show second image
    ax = fig.add_subplot(1,2,2)
    plt.imshow(imgB, cmap = plt.cm.gray)
    plt.axis("off")

    #show the images
    plt.show()


