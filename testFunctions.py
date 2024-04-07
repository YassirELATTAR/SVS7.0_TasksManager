import tkinter as tk
from tkinter import filedialog
import os
import csv
from collections import defaultdict
import re

def merge_csv_files(directory):
    # Create the combinedCSV directory (if it doesn't exist)
    combined_dir = os.path.join(directory, "combinedCSV")
    os.makedirs(combined_dir, exist_ok=True)  # Safely create the directory

    # Dictionary to store header sets and corresponding data lists
    header_data = defaultdict(list)

    # Iterate through CSV files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)  # Read the header row

                # Convert header list to a tuple
                header_tuple = tuple(header)

                # Check if header is already encountered
                if header_tuple not in header_data:
                    header_data[header_tuple] = []

                header_data[header_tuple].extend(reader)

    # Write merged data to separate CSV files
    for header, data_rows in header_data.items():
        output_filename = os.path.join(combined_dir, f"merged_{','.join(header)}.csv")
        with open(output_filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header) 
            writer.writerows(data_rows) 

    print(f"Merged CSV files saved to: {combined_dir}")

def select_file():
        root = tk.Tk()
        root.withdraw()
        selected_file = filedialog.askopenfilename(
            title="Select file to process",
            filetypes=[
                ("All Files", "*")        # Allow all other file types
            ]
        )
        return selected_file


def getOutputDirectory():
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory(title="Select output folder")
        return folder_path



def extract_lines_between_conditions(filename, start="", end=""):
    if start == "":
        start = "^"
    if end == "":
        end="$"
    pattern = fr"{start}(.*?){end}"  # Regex pattern with optional start and end
    matching_lines = []

    with open(filename, "r") as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                matching_lines.append(match.group(0))  # Extract the matched text

    return matching_lines

selected = select_file()

start_marker = "an"
end_marker = "@mac.com"
extracted_content = extract_lines_between_conditions(selected, start_marker, end_marker)
for line in extracted_content:
    print(line)

print(len(extracted_content))
