import cv2

# Load image
image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Histogram Equalization
equalized = cv2.equalizeHist(gray)

# Save output
cv2.imwrite("images/output/histogram_equalization.jpg", equalized)

print("Histogram equalization completed successfully!")