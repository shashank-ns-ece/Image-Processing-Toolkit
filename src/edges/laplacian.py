import cv2

# Load image
image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Laplacian
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Convert back to uint8
laplacian = cv2.convertScaleAbs(laplacian)

# Save output
cv2.imwrite("images/output/laplacian.jpg", laplacian)

print("Laplacian edge image saved successfully!")