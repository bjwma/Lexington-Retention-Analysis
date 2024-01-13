import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20221216213408/https://www.lexingtonma.org/staff-directory/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the parent container of the table if needed
    parent_container = soup.find('div', class_='dataTable')

    # Adjust the find method based on the HTML structure
    table = parent_container.find('table', class_='directory-table') if parent_container else soup.find('table', class_='directory-table')

    if table:
        for row in table.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            row_data = [cell.text.strip() for cell in cells]
            print(row_data)
    else:
        print("Table not found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")