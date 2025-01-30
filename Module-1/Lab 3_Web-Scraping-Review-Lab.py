from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a webpage

url = "http://www.ibm.com"

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

# create a soup object using the variable 'data'
soup = BeautifulSoup(data,"html.parser")

# in html anchor/link is represented by the tag <a>
for link in soup.find_all('a'):
    print(link.get('href'))

for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link.get('src'))


#Scrape data from html tables
#The below URL contains a html table with data about colors and color codes.
URL = ("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/"
       "datasets/HTMLColorCodes.html")

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(URL).text

soup = BeautifulSoup(data,"html.parser")

#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>

for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].getText() # store the value in column 3 as color_name
    color_code = cols[3].getText() # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))

