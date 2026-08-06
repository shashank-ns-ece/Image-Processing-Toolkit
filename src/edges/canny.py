import cv2

# Load image
image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
canny = cv2.Canny(gray, 100, 200)

# Save output
cv2.imwrite("images/output/canny.jpg", canny)

print("Canny edge image saved successfully!")