# Document-Scanner
Document scanning can be broken down into three distinct and simple steps.
The first step is to apply edge detection.
The second step is to find the contours in the image that represent the document we want to scan.
And the final step is to apply a perspective transform to obtain a top-down, 90-degree view of the image, just as if we scanned the document.
Optionally, you can also apply thresholding to obtain a nice, clean black and white feel to the piece of paper.
# OCR
Extract text from the scanned image and displays it.

# NLP
Next we can do anything with this text using NLP techniques.

# STEPS
1. Clone this repository.
2. pip install > requirements.txt
3. python scanner.py --image <image_name>
4. python ocr.py --image <image_name>
