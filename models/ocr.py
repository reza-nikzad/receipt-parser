import cv2
import pytesseract

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return thresh

def extract_text_from_image(image_path):
    preprocessed_img = preprocess_image(image_path)
    text = pytesseract.image_to_string(preprocessed_img)
    return text



