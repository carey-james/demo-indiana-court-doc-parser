# demo-indiana-court-doc-parser
A demonstration of using Python to parse Indiana court documents.

This demonstration code reads in PDFs of complaints in civil cases, searches those PDFs for the case number and for the amount being sued for, and outputs the results to a CSV file.

It was designed with PDFs from the [mycase.IN.gov](https://public.courts.in.gov/mycase/) case search, manually pulled based on a random search of civil cases. To replicate, download a group of PDFs from this site and follow the instructions below.

**Comply with all [Terms of Use of the Indiana Courts MyCase website](https://www.in.gov/courts/policies/tou-mycase/) while doing this. Do not overburden the site or use it for commercial use. Contact the Indiana Judicial Branch if you are a private or academic researcher looking for bulk data access.**

## Assumptions of the Parser
The parser is just intended as an example and makes several assumptions which may be false for some number of court records:
* The PDF provided is a Civil Case from Indiana.
* The PDF is the Complaint from that case.
* The Complaint has the Case Number in the following form: XXXXX-XXXX-XX-XXXXXX
* The Compliant lists the amount sought in the case in dollars, and this is the only dollar figure listed in the first 2 pages of the complaint.

For long term use these assumptions should be checked against the actual files parsed and the parser should be adapted to match the real needs of the parsing.

## Use
To use this parser:
1. Make sure Python 3 is installed on your system and up to date.
2. Install requirements in `requirements.txt`, using something like: `pip3 install -r ./requirements.txt`.
3. Place pdf files of Complaints in `/pdfs/`.
4. Run the parser: `python3 docParser.py`.
5. Look for the results in `/results/`.

## Purpose
This demonstration code was written by James Carey in Dec 2024 as an example of how an Indiana court could possibly parse complaint PDFs. It may also serve as a useful example of court PDF parsing for other researchers. It is not intended for any commercial or malicious purpose.

## License
MIT License

Copyright (c) 2024 James Carey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.