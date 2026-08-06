import cv2
import os

def main():
    # Load input image
    image = cv2.imread("images/input/sample.jpg")

    if image is None:
        print("Error: Image not found!")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create output folder if it doesn't exist
    os.makedirs("images/output", exist_ok=True)

    # Save grayscale image
    cv2.imwrite("images/output/grayscale.jpg", gray)

    # Show original image
    cv2.imshow("Original Image", image)

    # Show grayscale image
    cv2.imshow("Grayscale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()