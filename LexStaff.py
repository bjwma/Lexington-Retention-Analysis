import requests
from bs4 import BeautifulSoup
import csv

url = "https://web.archive.org/web/20200918133257/https://www.lexingtonma.org/staff-directory/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Adjust the find method based on the HTML structure
    table = soup.find('table', id="staffMembers")

    if table:
        # Open a CSV file for writing
        with open('LexData2020.csv', 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write header row if the table has header cells (th)
            header_row = [header.text.strip() for header in table.find_all('th')]
            if header_row:
                csv_writer.writerow(header_row)

            # Write data rows
            for row in table.find_all('tr'):
                cells = row.find_all(['td', 'th'])
                row_data = [cell.text.strip() for cell in cells]
                csv_writer.writerow(row_data)

        print("Table data successfully exported to 'LexData2023.csv'.")
    else:
        print("Table not found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")