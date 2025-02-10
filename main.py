from models import ocr

if __name__ == "__main__":
    image_path = "images/receipt1.jpg" 
    extracted_text = ocr.extract_text_from_image(image_path)
    print(extracted_text)