import cv2

def main():
    image = cv2.imread("images/input/sample.jpg")

    if image is None:
        print("Error: Image not found!")
        return

    cv2.imshow("Image Processing Toolkit", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()