import csv
import sys

# Ensure the correct number of command-line arguments
if len(sys.argv) != 3:
    print("Usage: python fixCsv.py <input_file> <output_file>")
    sys.exit(1)

# Get input and output file paths from command-line arguments
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# Read the tab-delimited CSV file
with open(input_file_path, "r") as infile:
    csv_reader = csv.reader(infile, delimiter='\t')
    
    # Create a list to hold the converted data
    converted_data = []

    # Iterate through each row in the input file
    for row in csv_reader:
        # Replace empty strings with null characters ('\0') to represent missing data
        converted_row = [field if field else '\0' for field in row]
        converted_data.append(converted_row)

# Write the converted data to the output file
with open(output_file_path, "w", newline="") as outfile:
    csv_writer = csv.writer(outfile, delimiter='\t', lineterminator='\n')
    csv_writer.writerows(converted_data)

print(f"CSV file with null characters saved to {output_file_path}")
