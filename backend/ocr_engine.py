import pytesseract
from PIL import Image
import cv2
import numpy as np

class OCREngine:
    @staticmethod
    def extract_text(image_path: str):
        """
        Preprocesses image and extracts text using Tesseract.
        """
        try:
            # Read image with OpenCV
            img = cv2.imread(image_path)
            
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Thresholding to help OCR
            _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            # OCR
            text = pytesseract.image_to_string(thresh)
            return text
        except Exception as e:
            return f"Error: {str(e)}"
