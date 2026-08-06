import cv2

image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Image not found")
    exit()

median = cv2.medianBlur(image, 9)

cv2.imwrite("images/output/median_blur.jpg", median)

print("Median blur image saved successfully!")