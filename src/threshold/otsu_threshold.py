import cv2

image = cv2.imread("images/input/sample.jpg")

if image is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, otsu = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

cv2.imwrite("images/output/otsu_threshold.jpg", otsu)

print("Otsu threshold completed successfully!")