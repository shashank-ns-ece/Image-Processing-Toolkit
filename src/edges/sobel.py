import cv2

# Load image
image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sobel X and Y
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine
sobel = cv2.addWeighted(
    cv2.convertScaleAbs(sobel_x),
    0.5,
    cv2.convertScaleAbs(sobel_y),
    0.5,
    0
)

# Save
cv2.imwrite("images/output/sobel.jpg", sobel)

print("Sobel edge image saved successfully!")