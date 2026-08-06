import cv2
import os


def load_image(path="images/input/sample.jpg"):
    image = cv2.imread(path)

    if image is None:
        raise FileNotFoundError(f"Unable to load image: {path}")

    return image


def save_image(image, filename):
    os.makedirs("images/output", exist_ok=True)

    output_path = os.path.join("images/output", filename)

    cv2.imwrite(output_path, image)

    print(f"Saved: {output_path}")


def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)