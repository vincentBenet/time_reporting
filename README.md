# time_reporting

This project aim to transform individuals times keeping files into a global one.

## Installation
* Place the folder V1.0 in your computer
* Run the .exe file
* Select the folder where .csv files are formated YYYY - MM - NAME.csv
* Gather the .csv result in the same folder

## Build from source
If you are not secure in running an external .exe file from an unknow person that ask you admin rights, you can compile yourself this project or run it directly in python.

### Run in python
* Install the last python version (check the checkbox to add python to your global path during installation)
* Clone this project to your computer
* run the file ~/source/time_reporting.py with the command `python ~/source/time_reporting.py` (replace ~ with the path of the project on your computer)

### Compile
* Check the content of all python file of the project. Make sure there isn't anything that is a security issue for your company.
* Install the cx_freeze compilator module with the command `pip install cx-Freeze`
* run the file ~/source/time_reporting.py with the command `python ~/source/time_reporting.py` (replace ~ with the path of the project on your computer)
* Gather the result generated in the folder ~/source/dist/
* You have now your own version of the project!
