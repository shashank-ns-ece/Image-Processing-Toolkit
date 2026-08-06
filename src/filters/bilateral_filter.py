import cv2

# Load image
image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Image not found")
    exit()

# Apply Bilateral Filter
bilateral = cv2.bilateralFilter(image, 9, 75, 75)

# Save output
cv2.imwrite("images/output/bilateral_filter.jpg", bilateral)

print("Bilateral filter image saved successfully!")