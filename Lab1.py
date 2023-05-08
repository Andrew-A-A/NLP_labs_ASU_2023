import pandas
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import pandas as pd
# region Read html file
with open('D:/Files/College/NLP/Labs/Lab1/mydoc.html') as f:
    html_doc = f.read()

# parsing
soup = BeautifulSoup(html_doc, 'html.parser')
# print tag with value
print(soup.b)
# print first occurrence value
print(soup.b.string)
# print all values
for x in soup.find_all('b'):
    print(x.string)
# endregion

# region Read URL
# read html file
response = urlopen('https://www.google.com/')
html_doc = response.read()
# Parsing
soup = BeautifulSoup(html_doc, 'html.parser')
# formatting parsed html file
strhtm = soup.prettify()
# print few lines
print(strhtm[:1000])
# endregion Read URL

# region Read and write json
dictionary = {
    "name": "Andrew",
    "height": 156,
    "weight": 56,
    "phonenumber": "0775000"
}
with open("D:/Files/College/NLP/Labs/Lab1/sample.json", 'w') as outfile:
    json.dump(dictionary, outfile)

with open("D:/Files/College/NLP/Labs/Lab1/sample.json", 'r') as outfile:
    mydict = json.load(outfile)
print(mydict)
# endregion

# region Read CSV files
data = pd.read_csv("D:/Files/College/NLP/Labs/Lab1/sample.csv")
print(data.head(5))
# endregion

# region HANDS ON
data = {'id': [1, 2, 3], 'name': ['Ali', 'Andrew', 'Alaa'], 'subject': ['lol1', 'lol2', 'lol3']}
df = pandas.DataFrame(data)
with open('test.csv', 'w') as file:
    df.to_csv(file)
# endregion
