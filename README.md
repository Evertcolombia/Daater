# Daater

# Installing

use python3, pip3, execute the command:

	$ pip3 install -r requirements.txt
	$ export LC_ALL=C.UTF-8
	$ export LANG=C.UTF-8


## setup

It will take the .csv files from your cwd path

- create  detail and online folders

	$ mkdir detail online

- copy in these folders the .csv files you want to use in the folder that corresponds

- enter in the detail file and run pwd

	-  cd detail/
	-  pwd
	
	
 	/root/Dateer/detail -> copy this path

- open the main.py file and chnage the paths in the follow lines

	15- onlinefile = readfile('/root/Daater/online')
	18- detailfile = readfile('/root/Daater/online')
	62- path = '/root/Daater/'

- save the changes

# run the code

	python3 main.py

- if the program ends will create a new .csv file

