# Excel2xmlMODS
Tools to create MODS XML records from an Excel spreadsheet.

This set of tools is for a workflow created for Alexandria Library Local History/Special Collections, that allows
metadata to be entered by volunteers into an Excel worksheet, which is converted into XML using OpenRefine and Python3.
The metadata can be entered as hundreds of different items in the spreadsheet, but the end result will be hundreds of XML
files named using the identifier and .xml. 

In addition to requiring Python 3, it is also recommended that OpenRefine be downloaded.

Create metadata using the MODSExcelTemplate.  Save the eventual file to be converted as a .csv.
Create a folder, naming it anything, but keep in mind to change the path accordingly in the xml_split_MODS.py.  This folder
  will be your "output path."  The Python file and later on, the MODSSource.txt file can live next to it (not in it).

Then move to OpenRefine.
    1. Click "Choose Files" and choose the .csv, then click "Next."
    2. Once spreadsheet loads, check it, then click "Create Project" at the top right.
    3. Click "Export" then "Templating" at the top right.
    4. Enter the template from the OpenRefine_MODS_Template.txt, then "Export" when done.
    5. Save the file as MODSSource.txt and move it to the same folder that the xml_split_MODS.py lives in.

Go to the command line change directory to the folder that the xml_split_MODS.py script lives in.
Run xml_split_MODS.py

If the end result in the command line is "All done!", then the xml files should be in the folder designated for output.
