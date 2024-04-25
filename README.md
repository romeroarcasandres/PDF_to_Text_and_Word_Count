# PDF_to_Text_and_Word_Count
It extracts text from PDF files in a selected directory and counts the total number of words in the extracted text files.

## Overview:
This script extracts the text of PDF files into text files (TXT format) and it generates a new "word-count.txt" file with the individual word counts (per file) and the total word count (the sum of all the files).

It prompts the user to select a directory using a file dialog, extracts the PDF files text into TXT files with the same name as the PDF files and saves them into a subdirectory named "converted_files". 
Additionally, the script counts the total number of words in the extracted text files and generates a word-count report in the same subdirectory.

## Requirements:
Python 3

PyPDF2 library (for PDF handling)

tkinter library (utilized for file dialog)

os library (for file path operations)

## Files
extract_pdf_text_word-count.py

## Usage
1. Run the script.
2. A file dialog will prompt you to select the PDF files directory.
3. After selecting the directory, the script will extract the PDFs content into TXT files in the "converted_files" subdirectory.
4. It generates a word-count report named "word-count.txt" in the "converted_files" subdirectory.

See "PDF_to_Text_and_Word_Count_1.JPG", "PDF_to_Text_and_Word_Count_2.JPG" and "PDF_to_Text_and_Word_Count_3.JPG".

## Important Note
Ensure that the selected directory contains valid editable PDF files.

Accurate text extraction and word count cannot be guaranteed with non-editable PDF files.

The word-count report ("word-count.txt") includes individual file word counts and the overall directory word count.

## License
This project is governed by the GNU Affero General Public License v3.0. For comprehensive details, kindly refer to the LICENSE file included with this project.
