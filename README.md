# PDF OCR Keyword Extractor

## Description
PDF Keyword Extractor is a Python script that extracts text from PDF files using OCR (Optical Character Recognition) and searches for specified keywords within the extracted text. It can process multiple PDF files within a given folder and generates a CSV file containing the keywords found along with their context within the PDF files.

## Dependencies
- Python 3.x
- pytesseract
- Pillow (PIL)
- PyMuPDF (fitz)
- `tesseract` OCR engine

## Installation
1. Ensure you have Python installed on your system. If not, download and install it from [Python's official website](https://www.python.org/).
2. Install the required Python packages using pip:

```bash
pip install pytesseract pillow PyMuPDF
```
3. Install Tesseract OCR engine. You can download it from [Tesseract's GitHub page](https://github.com/tesseract-ocr/tesseract). Make sure to add its path to the system PATH or specify the path in the script.

## Usage
1. Clone or download the script to your local machine.
2. Ensure that your PDF files are stored in a folder accessible to the script.
3. Modify the script to specify the keywords you want to search for (`keywords` variable), the folder containing the PDF files (`folder_path`), and the output CSV file path (`output_file`).
4. Run the script using the command:


## Sample Usage
```python
# Define the keywords to search
keywords = ['keyword1', 'keyword2', 'keyword3', 'keyword4', 'keyword5', 'keyword6']

# Specify the folder path containing the PDF files
folder_path = '/path/to/pdf/files/'

# Specify the output CSV file path
output_file = 'output.csv'

# Set the path to the Tesseract executable (if not in the system PATH)
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# Call the function to search for keywords in the PDF files and generate the CSV file
search_keywords_in_folder(keywords, folder_path, output_file)
```

## Notes
Ensure that the Tesseract OCR engine is properly installed and accessible to the script.
Adjust the keyword list, folder path, and Tesseract executable path according to your requirements.
This script is designed for PDF files. Ensure your PDF files are in a readable format.
The script will generate a CSV file containing the keyword matches found along with their context within the PDF files.

## License
This script is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests on GitHub.

## Author
tomas7470

## Acknowledgments
This script utilizes pytesseract for OCR text extraction.
Special thanks to contributors of pytesseract, Pillow, and PyMuPDF for their valuable libraries.
Inspired by the need to efficiently extract and search for keywords within scan german contracts.

