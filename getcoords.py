import sys

# Ensure the correct number of command-line arguments
if len(sys.argv) != 3:
    print("Usage: python filter_data.py <input_filename> <output_filename>")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

# Define the coordinates of the bounding box
min_latitude = 50  # Southernmost point (Newfoundland)
max_latitude = 87.5  # Northernmost point (Greenland)
min_longitude = -90  # Westernmost point (Newfoundland)
max_longitude = -10  # Easternmost point (UK)

# Function to check if coordinates are within the bounding box
def is_within_bounding_box(latitude, longitude):
    return min_latitude <= latitude <= max_latitude and min_longitude <= longitude <= max_longitude

# Open the input file and create an output file for filtered entries
with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    # Read the header line
    header = infile.readline().strip().split('\t')

    # Find the indices of the latitude and longitude columns
    latitude_index = header.index('LATITUDE')
    longitude_index = header.index('LONGITUDE')

    # Write the header to the output file
    outfile.write('\t'.join(header) + '\t.\n')

    # Process the data lines
    for line in infile:
        fields = line.strip().split('\t')
        latitude = float(fields[latitude_index])
        longitude = float(fields[longitude_index])

        if is_within_bounding_box(latitude, longitude):
            outfile.write(line)

# Close the files
infile.close()
outfile.close()

