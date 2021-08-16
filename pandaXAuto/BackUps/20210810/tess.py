# We import the necessary packages
#import the needed packages
import cv2
import os, argparse
import pytesseract
from PIL import Image
import re











#We then Construct an Argument Parser
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",
                required=True,
                help="Path to the image folder")
ap.add_argument("-p","--pre_processor",
                default="thresh", 
                help="the preprocessor usage")
args=vars(ap.parse_args())
  
#We then read the image with text
images=cv2.imread(args["image"])
  
#convert to grayscale image
gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
  
#checking whether thresh or blur
if args["pre_processor"]=="thresh":
    cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
    print("This works 1")
if args["pre_processor"]=="blur":
    cv2.medianBlur(gray, 3)
    print("This works 1")
      
#memory usage with image i.e. adding image to memory
filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
#print(text)

with open("ocr-data.txt", "w") as file:
	file.write(text)








# with open("ocr-data.txt") as file:
# 	for line in file:
# 		survey_code = re.search(r'\d{4}-\d{4}-\d{4}-\d{4}-\d{4}-\d{2}', line, re.M|re.I)

# 		if survey_code != None:

# 			survey_code = str(survey_code.group()).split("-")
# 			print(survey_code)