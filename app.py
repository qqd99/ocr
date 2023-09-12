import cv2
import pytesseract

# Path to tesseract.exe (use raw string to avoid escaping)
tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Location of test image
image_path = "Untitled.png"

# Read the image directly as RGB
img = cv2.imread(image_path)

# Use pytesseract to get text boxes
boxes = pytesseract.image_to_data(img).splitlines()

# Iterate through the boxes
for i, box in enumerate(boxes[1:]):  # Start from index 1 to skip header
    b = box.split()
    if len(b) == 12:
        x, y, w, h = map(int, b[6:10])
        print(b[11])  # b[11] is text
        cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)

# Display the image
cv2.imshow('Result', img)
cv2.waitKey(0)
