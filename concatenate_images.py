#!/usr/bin/env python

import numpy as np
import cv2 
import matplotlib.pyplot as plt
import PIL.Image



for i in [x for x in range (1,226) if x!=101]:

	directory = f"/home/kate/catkin_ws/src/DATASETS/Dataset/{i}"
	img1 = cv2.imread(f"{directory}/rgb0_json/img.png")
	img2 = cv2.imread(f"{directory}/rgb1_json/img.png")

	im_h = cv2.hconcat([img1, img2]) 
	cv2.imwrite(f"{directory}/concatenated_rgb_image.png", im_h) 

	img1 = cv2.imread(f"{directory}/rgb0_json/label.png")
	img2 = cv2.imread(f"{directory}/rgb1_json/label.png")

	im_h = cv2.hconcat([img1, img2]) 
	cv2.imwrite(f"{directory}/concatenated_image.png", im_h) 

	labeled_im1 = f"{directory}/rgb0_json/label.png"
	labeled_im2 = f"{directory}/rgb1_json/label.png"

	img1 = np.array(PIL.Image.open(labeled_im1))
	img2 = np.array(PIL.Image.open(labeled_im2))

	out_labeled_image = np.concatenate((img1,img2), axis=1)
	cv2.imwrite(f"{directory}/concatenated_labeled_image.png", out_labeled_image)

# print(np.unique(out_labeled_image))
