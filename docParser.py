import os
import re
import PyPDF2
import csv

# Constants
# Locations of Files
PDF_DIR = './pdfs/'
RESULTS_DIR = './results/'

# Helper function to pull out the 
def match_helper(match):
	if match:
		return match.group(1)
	else:
		return ''

# Helper to normalize the amount results, removing spaces and commas
def money_normalizer(amount):
	if amount:
		return re.sub(r'[ ,]', '', amount)
	else:
		return ''

def process(pdf):
	result = {}

	# Read first two pages, as the amount is most often there
	reader = PyPDF2.PdfReader(os.path.join(PDF_DIR, pdf))
	page0 = reader.pages[0].extract_text()
	page1 = reader.pages[1].extract_text() if (len(reader.pages) > 1) else ''
	pages_text = page0 + page1
	
	# Regex patterns  to search for
	case_number_pattern = r'([A-Z\d]{5}-[A-Z\d]{4}-[A-Z]{2}-[A-Z\d]{6})'
	amount_pattern = r'(\$[ \d\.\,]*\.\d\d)'
	# Additional potential patterns
	# plaintiff_pattern = r'^(.*) No\..*\n(?=Plaintiff)'
	# defendant_pattern = r'^(.*) AmountClaimed.*\n(?=Defendant)'

	# Searching and storing the results of the patterns. Search is used to only get first match.
	result['case_number'] = match_helper(re.search(case_number_pattern, pages_text))
	result['amount'] = money_normalizer(match_helper(re.search(amount_pattern, pages_text)))
	# Additional potential searches
	# result['plaintiff'] = match_helper(re.search(plaintiff_pattern, pages_text))
	# result['defendant'] = match_helper(re.search(defendant_pattern, pages_text))

	return result

def main():
	# Set up empty dict for results
	results = {}

	# Load in the PDF info
	pdfs = [f for f in os.listdir(PDF_DIR) if f.endswith('.pdf') and os.path.isfile(os.path.join(PDF_DIR, f))]

	# For each PDF extract the case number and amount
	for pdf in pdfs:
		result = process(pdf)
		results[result['case_number']] = {'amount':result['amount']}

	# Save the results as a PDF
	with open(f'{RESULTS_DIR}results.csv', 'w', newline = '') as output_f:
		csv_writer = csv.writer(output_f)
		csv_writer.writerow(['case_number', 'amount'])
		for case in results:
			csv_writer.writerow([case,results[case]['amount']])

	print(f'All found case numbers and amounts have been written to: \n{RESULTS_DIR}results.csv \nWatch out for blank cells where results were not found.')

if __name__ == '__main__':
	main()