from PIL import Image
import pytesseract
from urllib import request

if __name__ == "__main__":
    # png = Image.open('test.png')
    # binary_data = request.urlopen('https://passport.baidu.com/cgi-bin/genimage?njG1406de672683f5d7027f15caa6015c008dcd5b06ba048a4f').read()
    # temp_file = open("genimage.png", 'wb')
    # temp_file.write(binary_data)
    # temp_file.close()
    png = Image.open('test.png')
    text = pytesseract.image_to_string(png, lang='chi_sim')
    print(text)
