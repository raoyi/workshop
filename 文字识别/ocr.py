from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open('txt.jpg')

print(pytesseract.image_to_string(img, lang = 'chi_sim'))
