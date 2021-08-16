
import re

with open("ocr-data.txt") as file:
	for line in file:
		survey_code = re.search(r'\d{4}-\d{4}-\d{4}-\d{4}-\d{4}-\d{2}', line, re.M|re.I)

		if survey_code != None:

			survey_code = str(survey_code.group()).split("-")
			print(survey_code)




