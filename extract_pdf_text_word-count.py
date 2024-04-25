import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog

def select_directory():
    """
    Prompts the user to select a directory and returns the selected directory path.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    directory_path = filedialog.askdirectory(title="Select Directory Containing PDF Files")
    return directory_path

def count_words_in_file(filename, encoding="utf-8"):
    """
    This function counts the number of words in a given text file.

    Args:
        filename: The path to the text file.
        encoding: The encoding of the file (e.g., "utf-8", "latin-1").

    Returns:
        The number of words in the file.
    """
    try:
        with open(filename, 'r', encoding=encoding) as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

def count_words_in_directory(directory, encoding="utf-8"):
    """
    This function counts the total words in all .txt files within a directory,
    printing individual file word counts, and the overall directory word count.

    Args:
        directory: The path to the directory containing the text files.
        encoding: The encoding of the files (e.g., "utf-8", "latin-1").

    Returns:
        The total word count for all text files in the directory.
    """
    total_word_count = 0
    word_count_data = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            word_count = count_words_in_file(file_path, encoding)
            total_word_count += word_count

            # Print individual file word count
            print(f"The file '{filename}' contains {word_count} words.")

            # Store filename and word count data
            word_count_data.append(f"{filename}\t{word_count}")

    # Print total word count for all files
    print(f"The directory '{directory}' contains a total of {total_word_count} words.")

    # Write word count data to word-count.txt
    with open(os.path.join(directory, "word-count.txt"), "w", encoding="utf-8") as count_file:
        # Write header
        count_file.write("Name of the file\tWord count\n")
        
        # Write data
        for line in word_count_data:
            count_file.write(line + "\n")
        
        # Write total word count
        count_file.write(f"Total\t{total_word_count}")

    return total_word_count

def pdf_to_text_directory(directory_path):
    """
    Extracts text from all PDF files in a directory and writes them to .txt files.

    Args:
        directory_path: Path to the directory containing PDF files.
    """
    # Create the "converted_files" directory inside the selected directory
    output_directory = os.path.join(directory_path, "converted_files")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate through each file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            # Construct the full file path
            pdf_path = os.path.join(directory_path, filename)
            
            # Generate output text file path
            output_txt = os.path.join(output_directory, filename.replace('.pdf', '.txt'))

            # Extract text from PDF and save to text file
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                
                text = ""
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text() + "\n"

            with open(output_txt, 'w', encoding="utf-8") as txt_file:
                txt_file.write(text)

            print(f"Text extracted from {pdf_path} and saved to {output_txt}")

    # Count words in the "converted_files" directory
    word_count = count_words_in_directory(output_directory)
    print(f"Total word count in 'converted_files' directory: {word_count}")

if __name__ == "__main__":
    directory_path = select_directory()
    
    if directory_path:
        pdf_to_text_directory(directory_path)
