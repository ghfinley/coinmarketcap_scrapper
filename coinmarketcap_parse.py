from bs4 import BeautifulSoup

import pandas
import os
import glob

if not os.path.exists("parsed_files"): #check if the file path does not exist
	os.mkdir("parsed_files") #makes a folder named parsed_files

df = pandas.DataFrame() #create an empty data frame 


for file_name in glob.glob("html_files/*.html"): #go into html_files folder and look at the html files and it will run through each ome

	#file_name = "html_files/testing20211017134951.html" #name of the file you are pasring - only doing one file for now 

	#Place Time Stamp 
	scrape_time = os.path.basename(file_name).replace("testing","").replace(".html","")

	f = open(file_name,"r") # open the connection to the file and place the file in a variable f 

	soup = BeautifulSoup(f.read(),"html.parser") #use beautifulsoup to read f

	f.close() #close the connection to f as it is now in the soup

	#now the HTML content is in the soup and we are finding what we need for data analysis 

	tbody = (soup.find("tbody")) #can use this trick if only one tbody in the HTML to reduce what you have to go through 

	currency_rows = tbody.find_all("tr") #the rows are shown as tr in the html and we place them all in a new variable, this includes all the trs in the tbody


	for currency_row in currency_rows:  #Goes to the first row in all the rows and does this until it has run on every row 
		#currency_row = currency_rows[0] #place a specifc row in a variable - no For loop


		currency_columns = currency_row.find_all("td") # this is all the collumns in the specific row we listed above 
		
		if len(currency_columns)>5:
			print(scrape_time)

			
			currency_name = currency_columns[2].find("p").text # the Name is located in row 0 column 2 inside the p tab and only text there


			currency_price = currency_columns[3].find("a").text.replace("$","").replace(",","") # this prints the collumn we want from the table and specified row, a is the last tab and we want the tet in the a tab 

			
			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text #this will get you to the p tab with the ticker symbol 

			
			currency_market_cap = currency_columns[6].find("p").find("span",{"class":"sc-1ow4cwt-1"}).text.replace("$","").replace(",","") # use replace to take out the $ and , 

			currency_link = currency_columns[2].find("a")["href"]

		
			currency_image = currency_columns[2].find("img")["src"]

			#now we wnat to wrap the whole thing in a for loop so that we can pull out every entry 

			##Place the variables into the data frame df

			df = df.append({
				'time' : scrape_time,
				'name':currency_name,
				'price':currency_price, 
				'symbol':currency_symbol, 
				'marketcap': currency_market_cap, 
				'link': currency_link, 
				'image': currency_image
				},ignore_index = True
				)
				
			



df.to_csv("parsed_files/coinmarketcap_dataet.csv")