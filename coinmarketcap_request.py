import urllib.request #imports the command library

import os #import the operating system 

import time #import time 

import datetime #import date and time package to write time in file name 

if not os.path.exists("html_files"): #check if the file path does not exist
	os.mkdir("html_files") #makes a folder named html_files

for i in range(5):  #create a for loop to download data multiple times
	current_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S") #use the datetime command to get the time stamp all in numbers
	print(current_time) #print the current time, this will show that something is printing in the for loop as good practice 

	f = open("html_files/testing" + current_time + ".html","wb",) #opening a connection to the new file testing.html in the html_files folder

	response = urllib.request.urlopen("http://coinmarketcap.com/") #puts the request for the url in a variable 

	html = response.read() #allows the html to be in a variable 

	f.write(html) #write the html to the file that we opened 
	f.close() #close the connection to the file 

	time.sleep(30) #tell python how long to wait until it runs the loop again 







