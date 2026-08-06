import cv2

image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imwrite("images/output/binary_threshold.jpg", binary)

print("Binary threshold completed successfully!")