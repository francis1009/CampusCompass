from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_secondary_schools_in_Singapore"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
soup2 = soup.find('table', class_="wikitable sortable")
soup3 = soup2.find_all("th")
table_titles = [title.text.strip() for title in soup3]
print(table_titles)
soup4 = soup2.find_all("tr")
for row in soup4:
    row_data = row.find_all("td")
    indiv_row_data = [data.text.strip() for data in row_data]
    print(indiv_row_data)