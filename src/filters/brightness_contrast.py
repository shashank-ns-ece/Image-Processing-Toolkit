import cv2

image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Image not found")
    exit()

alpha = 1.2
beta = 20

result = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

cv2.imwrite("images/output/brightness_contrast.jpg", result)

print("Brightness & Contrast image saved successfully!")