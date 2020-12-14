# Log Analyzer Script

## 365-Widgets Grading System

The project reads the data file and grades the devices as per standard.

## Getting Started

Copy the script and data file to a folder on your computer. 

### for command prompt
* open command prompt
* change directory to the folder containing script and data file
* Run the script by entering the following command
> python log_analyzer.py

### for IDE
* open the program in your IDE such as Visual Studio Code or Thonny
* run the script

### Prerequisites

You need to have python installed on your system. The script also requires numpy.
If you are working on Ubuntu, you can install python and numpy running the following command:
> apt-get install python3 python3-numpy -y

## Running the tests

You may change the data in data.txt file. Or replace the file with another set of data to test.


## Create Docker image 
### Build Docker image Run
> docker build -t <your_username>/my-repo 

### Run Docker container
> docker run -it <your_username>/my-repo
### To Run my image 
> docker run -it bekosh94/log_analyzer:v1
