# Image Processing Toolkit

A modular image processing toolkit developed using **Python** and **OpenCV**. This project demonstrates fundamental image processing techniques including image enhancement, filtering, edge detection, thresholding, and morphological operations.

---

## Features

### Image Enhancement
- Grayscale Conversion
- Brightness & Contrast Adjustment
- Histogram Equalization

### Noise Reduction
- Gaussian Blur
- Median Blur
- Bilateral Filter

### Edge Detection
- Sobel Edge Detection
- Laplacian Edge Detection
- Canny Edge Detection

### Thresholding
- Binary Threshold
- Adaptive Threshold
- Otsu Threshold

### Morphological Operations
- Erosion
- Dilation
- Opening
- Closing

---

## Project Structure

```text
Image-Processing-Toolkit
│
├── images
│   ├── input
│   └── output
│
├── src
│   ├── filters
│   ├── edges
│   ├── histogram
│   ├── threshold
│   ├── morphology
│   ├── transform
│   └── utils
│
├── tests
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/shashank-ns-ece/Image-Processing-Toolkit.git

cd Image-Processing-Toolkit

python -m venv .venv

pip install -r requirements.txt
```

---

## Running an Algorithm

Example:

```bash
python src/edges/canny.py
```

Output images are saved in:

```text
images/output/
```

---

## Technologies Used

- Python
- OpenCV
- NumPy
- Git
- GitHub

---

## Current Progress

- ✅ Image Enhancement
- ✅ Noise Reduction
- ✅ Edge Detection
- ✅ Thresholding
- ✅ Morphological Operations
- ⏳ Image Transformations
- ⏳ Performance Benchmarking
- ⏳ Unit Testing

---

## Future Improvements

- Image Transformations
- Batch Image Processing
- Performance Analysis
- Automated Testing
- GUI Application