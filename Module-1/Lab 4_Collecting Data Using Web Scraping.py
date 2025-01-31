from bs4 import BeautifulSoup
import requests
import pandas as pd


#this url contains the data you need to scrape
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
# get the contents of the webpage in text format and store in a variable called response
response  = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Check if the request was successful
if response.status_code == 200:

    # Find the table containing the data
    table = soup.find('table')  # Finds the first table on the page

    # Extract the table rows (skip the header row)
    rows = table.find_all('tr')[1:]

    #  Extract data from each row
    data = []
    for row in rows:
        cols = row.find_all('td')  # Extract all columns in the row
        language = cols[1].text.strip()  # Language name
        salary = cols[3].text.strip()  # Annual Average Salary
        data.append([language, salary])

    #  Create a pandas DataFrame
    df = pd.DataFrame(data, columns=['Language Name', 'Annual Average Salary'])

    # Display the DataFrame
    print(df)

else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")

df.to_csv("popular-languages.csv", index=False)


