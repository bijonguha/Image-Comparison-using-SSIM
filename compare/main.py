#!/usr/bin/env python
#script to compare ssim and mse methoda

#standard library
import argparse

#3rd party lib
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Image Comparison SSIM and MSE')
	parser.add_argument('reference', metavar='REF', help='Reference Image')
	parser.add_argument('query',metavar='QRY', help='Query Image')

	args = parser.parse_args()

	img1 = cv2.imread(args.reference,0)
	img2 = cv2.imread(args.query,0)

	getattr(__import__('compare'), 'compare_images')(img1, img2)