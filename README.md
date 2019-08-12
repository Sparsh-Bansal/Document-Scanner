# Document-Scanner
Document scanning can be broken down into some distinct and simple steps.
1. Thresholding of image toremove noise in the image.
2. Appling edge detection(Canny).
3. Find the contours in the image that represent the document we want to scan.
4. Applying a perspective transform to obtain a top-down, 90-degree view of the image, just as if we scanned the document.
5. Finally Applying thresholding to obtain a nice, clean black and white feel to the piece of paper.
# OCR
Extract text from the scanned image and displays it.

# NLP
Next we can do anything with this text using NLP techniques.

# STEPS
1. Clone this repository.
2. pip install > requirements.txt
3. python scanner.py --image <image_name>
4. python ocr.py --image <image_name>
5. Run Flask Server for practical application
# NOTE:
For better results : 
1. Image should be clicked on 'dark againstbright background' or 'bright against dark background'.
2. Image size should be (2500-3500)*(2000-3000)
3. There should be background around four edges of the image.

These points should be taken care for obtaining better result than the normal result. 
(NOTE)At last user can itself crop its document if not satisfied with the output.(yet to implement)
# Results

<p float="left">
  <img src="images/desk.jfif" width="400" height="600" />
  <img src="output/desk_detected.jpg" width="400" height="600" /> 
</p>
<p float="left">
  <img src="images/test.jpg" width="400" height="600" />
  <img src="output/test_detected.jpg" width="400" height="600" /> 
</p>
<p float="left">
  <img src="images/notes2.jpg" width="400" height="600" />
  <img src="output/notes2_detected.jpg" width="400" height="600" /> 
</p>
<p float="left">
  <img src="images/page.jpg" width="400" height="600" />
  <img src="output/page_detected.jpg" width="400" height="600" /> 
</p>
<p float="left">
  <img src="images/IMG_20190703_104040.jpg" width="400" height="600" />
  <img src="output/IMG_20190703_104040_detected.jpg" width="400" height="600" /> 
</p>
<p float="left">
  <img src="images/IMG_20190705_130325.jpg" width="400" height="600" />
  <img src="output/IMG_20190705_130325_detected.jpg" width="400" height="600" /> 
</p>
<p float="left">
  <img src="images/IMG_20190704_103211.jpg" width="400" height="600" />
  <img src="output/IMG_20190704_103211_detected.jpg" width="400" height="600" /> 
</p>
<p float="left">
  <img src="images/IMG_20190703_132124.jpg" width="400" height="600" />
  <img src="output/IMG_20190703_132124_detected.jpg" width="400" height="600" /> 
</p>
# More Results at images and output folder.
