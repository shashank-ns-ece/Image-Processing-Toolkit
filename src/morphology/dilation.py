import cv2
import numpy as np

image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(gray, kernel, iterations=1)

cv2.imwrite("images/output/dilation.jpg", dilation)

print("Dilation completed successfully!")