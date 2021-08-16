from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time, re

#Find the Survey Code on the file that is populated with the OCR data (the data that tesseract extrapulated from the picture of the receipt)
with open("ocr-data.txt") as file:

	for line in file:
		survey_code = re.search(r'\d{4}-\d{4}-\d{4}-\d{4}-\d{4}-\d{2}', line, re.M|re.I)

		if survey_code != None:
			survey_code = str(survey_code.group()).split("-")
			print(survey_code)
			break

#Path string that works with the selenium library
PATH = "/mnt/c/Program Files (x86)/chromedriver.exe"

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


################################EXIT#######################################
exit()
################################EXIT#######################################

search = driver.find_element_by_xpath("//input[@id='NextButton']")
search.click()