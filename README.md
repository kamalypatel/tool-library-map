# Creating the Tool Library Yearly Membership Map

You should be able to utilize this python script to generate a heatmap with the Geo Coordinates (latitude,longitude) values of members to get an idea of where concentrations of membership exist.

To get the list of longitudes and latitudes, you'll have to export the CSV list of members from MyTurn that have their addresses.

Then you'll have to import that CSV into Google Sheets.

Then download the GeoCode by Awesome Table extension for Google Sheets: https://workspace.google.com/marketplace/app/geocode_by_awesome_table/904124517349

This extension will be used to automatically obtain the Latitude and Longitude values from the Membership Addresses.

To use the extension on data, just have the address information without "Address 2" inside the sheet. If the addresses are not concatenated into 1 column as a complete value (for example, "701 Ellicott Street Buffalo NY 14203" all inside a single cell is considered concatenated into 1 column), then the GeoCode extension has a handly tool to do that or you can use the CONCATENATE() function within Google Sheets.

If the GeoCode extension is maxed out, then you can always wait to code the rest of the values on a different day or code half on 1 Google Account and another half on a different Google Account.

Then once you have all the Lat and Long values, put them into a CSV where the headers of the columns are "Latitude" and "Longitude" for columns A and B. Then each row below that will have a coordinate. Make sure this file is called "latlongvalues.csv".