import cv2
from PIL import Image
import pytesseract
import pandas as pd
from pytesseract import Output
from matplotlib import pyplot as plt
import re
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
csv_folder_path = 'final_deliverable/csv'
img_folder_path = 'final_deliverable/img'
txt_folder_path = 'final_deliverable/txts'



def accuracy_on_keywords(ocr_result):
    keywords = {"TIME": 7, "FIELD": 1, "REPORT": 1, "#": 3, "TEST": 2, "PHASE": 2, "OF": 2, "DAY": 2, "ELAPSED": 2, "FLOW": 1, "SHUTIN": 1, "FINAL": 1, "FLOW": 1, "PAGE": 1, "BOT": 4, "HOLE": 4, "he.*o": 107}
    keywordsFound = 0
    for token in keywords.keys():
        numOfTokenFound = len(re.findall(token, ocr_result))
        keywordsFound += numOfTokenFound
        
    correctSum = sum(keywords.values())
    absDifference = abs(correctSum - keywordsFound)
    accuracy = round((correctSum - absDifference) / correctSum * 100, 2)
    print("\nCORRECT SUM OF KEYWORDS: {}\nDETECTED OCR KEYWORDS: {}\n*******************************\nACCURACY ON KEYWORDS: {}%\n".format(correctSum, keywordsFound, accuracy))
     

        
def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)

    height, width  = im_data.shape[:2]
    
    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()
    
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

img_files = [f for f in os.listdir(img_folder_path) if f.lower().endswith('.jpg')]


for img_file in img_files:
    # Construct the full path to the input image
    img_path = os.path.join(img_folder_path, img_file)
    
    # Read the image using OpenCV
    im = cv2.imread(img_path)
    
    # Perform image processing steps (grayscale, thresholding, etc.)
    gray_image = grayscale(im)
    cv2.imwrite("ocr_ver1/temp/gray.jpg", gray_image)
    gray_file = "ocr_ver1/temp/gray.jpg"

    thresh, im_bw = cv2.threshold(gray_image, 210, 230, cv2.THRESH_BINARY)
    cv2.imwrite("ocr_ver1/temp/bw_image.jpg", im_bw)
    bw_file = "ocr_ver1/temp/bw_image.jpg"

    # Perform OCR on the processed image
    img_test = Image.open(bw_file)
    custom_config = r'-l eng_final_model'
    ocr_result = pytesseract.image_to_string(img_test, config=custom_config)
    
    # Save the OCR result into a text file in the 'txts' folder
    txt_file_path = os.path.join(txt_folder_path, os.path.splitext(img_file)[0] + '.txt')
    with open(txt_file_path, 'w') as txt_file:
        txt_file.write(ocr_result)

# List all TXT files in the 'txts' folder
txt_files = [f for f in os.listdir(txt_folder_path) if f.lower().endswith('.txt')]

for txt_file in txt_files:
    # Construct the full path to the input text file
    txt_path = os.path.join(txt_folder_path, txt_file)

    # Read the content of the text file as a single string
    with open(txt_path, 'r') as txt_file:
        data = txt_file.read()

    # Split the data into lines
    lines = data.strip().split('\n')

    # Initialize lists to store the extracted data
    time = []
    date = []
    elapsed = []
    delta = []
    bot_hole_temp = []
    bot_hole_psi = []

    # Process each line
    for line in lines:
        parts = line.split()
        if len(parts) == 6:
            time.append(parts[0])
            date.append(parts[1])
            elapsed.append(parts[2])
            delta.append(parts[3])
            bot_hole_temp.append(parts[4])
            bot_hole_psi.append(parts[5])

    # Create a Pandas DataFrame
    df = pd.DataFrame({
        'Time': time,
        'Date': date,
        'Elapsed': elapsed,
        'Delta': delta,
        'Bot Hole Temp': bot_hole_temp,
        'Bot Hole PSI': bot_hole_psi
    })

    # Construct the full path to the output CSV file
    print(csv_folder_path)
    csv_file_path = os.path.join(csv_folder_path, os.path.splitext(txt_path)[0] + '.csv')

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)








img_test = Image.open(bw_file)
# custom_config = r'-l eng --oem 3 --psm 6 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-:.$%./@& *"'
custom_config = r'-l eng_final_model'

ocr_result = pytesseract.image_to_string(img_test, config=custom_config)
print(ocr_result)
