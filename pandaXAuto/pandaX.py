#! /usr/bin/env python
# -*- coding: utf-8 -*-


#For Selenium (does the automatic web clicking/filling out) 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#For Tesseract (the library that reads the receipt image)
import cv2
import os, argparse
import pytesseract
from PIL import Image

#For various other utilities
import time
import re

#Path string that works locating the selenium library
PATH = "/mnt/c/Program Files (x86)/chromedriver.exe"

def get_survey_code_from_image():
	#We then read the image with text
	images=cv2.imread("New Recipts/image000000.jpg")
	  
	#convert to grayscale image
	gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)

	#memory usage with image i.e. adding image to memory
	filename = "{}.jpg".format(os.getpid())
	cv2.imwrite(filename, gray)
	text = pytesseract.image_to_string(Image.open(filename))
	os.remove(filename)
	#print(text)

	with open("ocr-data.txt", "w") as file:
		file.write(text)	



def data_sifting():
	#Find the Survey Code on the file that is populated with the OCR data (the data that tesseract extrapulated from the picture of the receipt)
	with open("ocr-data.txt") as file:

		for line in file:
			survey_code = re.search(r'\d{4}-\d{4}-\d{4}-\d{4}-\d{4}-\d{2}', line, re.M|re.I)

			if survey_code != None:
				survey_code = str(survey_code.group()).split("-")
				return survey_code
				break


def execution(survey_code):
	driver = webdriver.Chrome(PATH)

	driver.get("https://www.pandaguestexperience.com/?AspxAutoDetectCookieSupport=1")

	search = driver.find_element_by_xpath("//input[@title='Input digits 1-4 of survey code']")
	search.send_keys(survey_code[0])

	search = driver.find_element_by_xpath("//input[@title='Input digits 5-8 of survey code']")
	search.send_keys(survey_code[1])

	search = driver.find_element_by_xpath("//input[@title='Input digits 9-12 of survey code']")
	search.send_keys(survey_code[2])

	search = driver.find_element_by_xpath("//input[@title='Input digits 13-16 of survey code']")
	search.send_keys(survey_code[3])

	search = driver.find_element_by_xpath("//input[@title='Input digits 17-20 of survey code']")
	search.send_keys(survey_code[4])

	search = driver.find_element_by_xpath("//input[@title='Input digits 21-22 of survey code']")
	search.send_keys(survey_code[5])

	search = driver.find_element_by_xpath("//input[@value='Start']")
	search.click()

	search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[1]")
	search.click()

	search = driver.find_element_by_xpath("//input[@id='NextButton']")
	search.click()

	##############################################

	i = 0
	while i != 2:
		search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[1]")
		search.click()

		search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[6]")
		search.click()

		search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[11]")
		search.click()

		search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[16]")
		search.click()

		search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[21]")
		search.click()

		search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[26]")
		search.click()

		search = driver.find_element_by_xpath("//input[@id='NextButton']")
		search.click()

		i = i + 1
		time.sleep(.2)

	search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[1]")
	search.click()

	search = driver.find_element_by_xpath("//input[@id='NextButton']")
	search.click()


	search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[2]")
	search.click()

	search = driver.find_element_by_xpath("//input[@id='NextButton']")
	search.click()


	search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[1]")
	search.click()

	search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[6]")
	search.click()

	search = driver.find_element_by_xpath("//input[@id='NextButton']")
	search.click()


	search = driver.find_element_by_xpath("//textarea[@id='S000077']")
	search.send_keys("Kim is the all-time best!!! I'm always very satisfied at this\
	 location. Ever since I realized that there are great healthy options here,\
	 I stopped going to the choptle that is located next door to this location.")

	search = driver.find_element_by_xpath("//input[@id='NextButton']")
	search.click()


	search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[1]")
	search.click()

	search = driver.find_element_by_xpath("//input[@id='NextButton']")
	search.click()


	search = driver.find_element_by_xpath("//input[@id='S000084']")
	search.send_keys("Kim")

	search = driver.find_element_by_xpath("//input[@id='NextButton']")
	search.click()


	search = driver.find_element_by_xpath("(//span[@class='radioSimpleInput'])[4]")
	search.click()

	search = driver.find_element_by_xpath("//input[@id='NextButton']")
	search.click()


	search = driver.find_element_by_xpath("(//option[@value='2'])[1]")
	search.click()

	search = driver.find_element_by_xpath("(//option[@value='3'])[2]")
	search.click()

	search = driver.find_element_by_xpath("(//option[@value='9'])[3]")
	search.click()

	search = driver.find_element_by_xpath("(//option[@value='9'])[4]")
	search.click()

	search = driver.find_element_by_xpath("//input[@id='NextButton']")
	search.click()

	time.wait(100)

def main():
	get_survey_code_from_image()
	survey_code = data_sifting()
	execution(survey_code)
main()