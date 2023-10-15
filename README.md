# eBird data to Google Earth

This repository contains files and instructions for processing eBird data for a specific bird species and visualizing it in Google Earth Pro.

## Prerequisites

Before you begin, make sure you have the following:

- **Python**: You need Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/) if it's not already installed.

- **Google Earth Pro**: Download and install Google Earth Pro from [Google Earth Pro](https://www.google.com/earth/versions/).

- **eBird Data**: To obtain the initial data, you need to request data from eBird for a specific bird species. Visit the [eBird website](https://ebird.org) and follow their instructions to request the data for your species of interest.

## Obtaining and Processing eBird Data

1. **Request Data from eBird**:
   - Visit the eBird website and log in or create an account if you don't have one.
   - Use the eBird data request tools to specify your bird species and geographic region. Request the data in the desired format (e.g., CSV).

2. **Download and Unzip Data**:
   - After your data request is processed, you will receive an email with a link to download the data. Follow the link to download the data file, which is typically in ZIP format.

   - Extract the contents of the ZIP file to a directory of your choice. You should find a text file (e.g., `ebd.txt`) that contains the eBird data for your species and region.

3. **Run the getcoords.py file**:
   - When you are ready to trim all of the observations for all of the world for your species data, manually edit the coordinates in `getcoords.py` to have the bounding box you would like. 

   - Then, run this file by:

   ```bash
   python getcoords.py ebd_*.txt input.txt
   ```

   - Of course, you can use a different name than `input.txt`, as that is not the best name here. But it sets you up for the following.

3. **Prepare Data for Google Earth**:
   - Use the provided Python script `convert_csv.py` to convert the `ebd.txt` file into a CSV file suitable for Google Earth Pro.

   - Run the script using the following command, replacing `input.txt` with your downloaded eBird data and `output.csv` with the desired output file name:

     ```bash
     python convert_csv.py input.txt output.csv
     ```

   - This script will replace empty fields with null characters (`\0`) to represent missing data. It is suggested you change the name to match the name of the species you are uploading.

## Visualizing Data in Google Earth Pro

1. **Open Google Earth Pro**:
   - Launch Google Earth Pro on your computer.

2. **Import Data**:
   - In Google Earth Pro, go to "File" > "Open" and select the converted CSV file (`output.csv`) generated in the previous step.

   - Ensure that you configure the import settings correctly, specifying the delimiter (usually tab) and column assignment.

3. **Customize Data**:
   - Once your data is loaded into Google Earth Pro, you can customize how the points are displayed, including icons, labels, and more.

4. **Explore and Analyze**:
   - Use Google Earth Pro's features to explore and analyze the eBird data. Click on data points to view metadata associated with each observation.

5. **Save or Share Map**:
   - If desired, you can save or export the map with your data in various formats, such as KML or KMZ, for sharing or further analysis.

## Contributing

If you would like to contribute to this project or report issues, please open an issue or pull request on the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.