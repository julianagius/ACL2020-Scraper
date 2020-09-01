"""
Python script to get paper titles and abstracts from ACL2020 and store them in a CSV file
"""

# Import required libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

titles = []
abstracts = ['']

URL = 'https://www.aclweb.org/anthology/volumes/2020.acl-main/'

# Get Response object for webpage
page = requests.get(URL)

# Parse webpage HTML and save as BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title text and append to list
title_paras = soup.find_all('p', class_='d-sm-flex align-items-stretch')

for para in title_paras:
    print()
    print('Title:')
    print(para.find_all('span', class_='d-block')[1].find('a', class_='align-middle').text)
    titles.append(para.find_all('span', class_='d-block')[1].find('a', class_='align-middle').text)

# Extract abstract text and append to list
abs_paras = soup.find_all('div', class_='card bg-light mb-2 mb-lg-3 collapse abstract-collapse')

for para in abs_paras:
    print()
    print(para.text)
    abstracts.append(para.text)

# Create pandas dataframe using list of titles & abstracts 
df = pd.DataFrame({'Title': titles, 'Abstract': abstracts})

# Save dataframe to csv
df.to_csv('ACL 2020 Papers.csv', index=False)
