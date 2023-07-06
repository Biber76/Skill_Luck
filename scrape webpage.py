import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://www.swissunihockey.ch/de/nla-nlb/l-upl-men/'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element containing the data
table = soup.find('table', class_='su-result')

print(table)

# # Extract the table headers
# headers = [header.text.strip() for header in table.find_all('th')]

# # Extract the table rows
# rows = []
# for row in table.find_all('tr'):
#     data = [cell.text.strip() for cell in row.find_all('td')]
#     if data:
#         rows.append(data)

# # Print the table headers
# print('\t'.join(headers))

# # Print the table rows
# for row in rows:
#     print('\t'.join(row))
