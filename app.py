from flask import Flask, request, jsonify, render_template
from models import ocr
import os

# Initialize the Flask app
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_receipt():
    """curl -X POST -F "file=@/path/to/your/image.jpg" http://localhost:5000/upload"""
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Save the file temporarily
    image_path = f"temp_{file.filename}"
    file.save(image_path)
    
    # Perform OCR to extract text from image
    extracted_text = ocr.extract_text_from_image(image_path)    
    
    return extracted_text

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6060))
    app.run(debug=True, host='0.0.0.0', port=port)