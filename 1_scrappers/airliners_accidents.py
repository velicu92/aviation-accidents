###############################################################################
### Scrape the airliners accidents database availabe at 
### https://aviation-safety.net/database/databases.php
###############################################################################

# import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
##import urllib2

# build the list of links to scrape





# read HTML URL

URL = "https://data.ntsb.gov/carol-main-public/query-builder?month=1&year=2024"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


print(page.text)



# read html data table
html_table = soup.find("table", attrs={"class":"wikitable"})
print(html_table)

# read the table lines added between <tr> tags
html_table_data = html_table.tbody.find_all("tr")
print(html_table_data)

# extract the table headers
table_head = []

for a in html_table_data[0].find_all('th'):
    table_head.append(a.text.replace('\n',''))

#extract data from the table

table_data = []
for a in html_table_data:
    row = []
    for b in a.find_all('td'):
        row.append(b.text.replace('\n',''))
    table_data.append(row)

# join the header and data into a pandas DataFrame
df = pd.DataFrame.from_records(table_data[1:len(table_data)], columns = table_head)


df.head()





data_url = 'https://data.ntsb.gov/carol-main-public/api/'
data = requests.get(data_url)

print(data.status_code)

print(data.json())



import urllib.request as req
from urllib.request import urlretrieve

url = "https://data.ntsb.gov/carol-main-public/query-builder?month=1&year=2024"
filename = "gdp_by_country.zip"


file = urlretrieve(url, filename)

print(file)

path, headers = urlretrieve(url, filename)
for name, value in headers.items():
    print(name, value)
    
soup = BeautifulSoup(page.content, "html.parser")

html = file.read()
    
    
    

with open("gdp_by_country.zip", mode="wb") as file:
    file.write(response.content)



url = 'https://data.ntsb.gov/carol-main-public/query-builder?month=1&year=2024'
r = requests.get(url)

print(r.content)


###############################################################################
## below is the solution by chat gpt

import requests

url = "https://data.ntsb.gov/carol-main-public/query-builder?month=1&year=2024"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the content of the response
    content = response.content

    # Save the content to a local file
    with open("downloaded_data.json", "wb") as file:
        file.write(content)
    
    print("Data downloaded successfully.")
else:
    print(f"Failed to download data. Status code: {response.status_code}")
###############################################################################


###############################################################################
## below is the solution by Copilot in Bing
import requests
from bs4 import BeautifulSoup

url = "https://data.ntsb.gov/carol-main-public/query-builder?month=1&year=2024"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    download_button = soup.find("a", {"class": "btn btn-primary btn-sm"})
    download_url = download_button["href"]
    download_response = requests.get(download_url)

    if download_response.status_code == 200:
        with open("ntsb_data.json", "wb") as f:
            f.write(download_response.content)
            print("Data downloaded successfully!")
    else:
        print(f"Failed to download data. Status code: {download_response.status_code}")
else:
    print(f"Failed to download data. Status code: {response.status_code}")
###############################################################################

url = "https://data.ntsb.gov/avdata/FileDirectory/DownloadFile?fileID=C%3A%5Cavdata%5Cavall.zip"
response = requests.get(url)


print(response.content)






import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlretrieve

url = "https://data.ntsb.gov/avdata/FileDirectory/DownloadFile?fileID=C%3A%5Cavdata%5Cavall.zip"
filename = "ntsb_data.zip"


file = urlretrieve(url, filename)

print(file)

import zipfile
with zipfile.ZipFile("ntsb_data.zip","r") as zip_ref:
    zip_ref.extractall()


from mdb_parser import MDBParser, MDBTable

aviation_db = MDBParser(file_path="avall.mdb")

print(aviation_db.tables)



###############################################################################
# The next part of the code has been taken from Rebase-website data
# https://www.rebasedata.com/python-read-mdb
###############################################################################


from meza import io
records = io.read('database.mdb') # only file path, no file objects
print(next(records))