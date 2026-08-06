import cv2

image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Image not found")
    exit()

blur = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imwrite("images/output/gaussian_blur.jpg", blur)

print("Gaussian blur image saved successfully!")