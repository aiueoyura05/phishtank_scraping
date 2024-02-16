import requests
from bs4 import BeautifulSoup
import csv
import time

with open('phish_urls2.csv','w', newline='',encoding='utf-8') as file:
    fieldname =['PhishID', 'PhishURL', 'Submitted', 'Valid', 'Online']
    writer =csv.DictWriter(file, fieldnames=fieldname)
    writer.writeheader()

    for i in range(50000):
        if i % 10 == 0:
            time.sleep(5)
            print("Sleeping for 5 seconds")
        url = "https://phishtank.org/phish_archive.php?page="+str(i)
        response = requests.get(url)

        if response.status_code ==  200:
            soup = BeautifulSoup(response.text, 'html.parser')
            rows = soup.find_all('tr')
            for row in rows[1:]:
                cells =row.find_all('td')
                phish_id = cells[0].find('a').text
                phish_url = cells[1].text.split('\n')[0].strip()
                username = cells[2].find('a').text
                valid = cells[3].text.strip()
                online = cells[4].text.strip()
                writer.writerow({'PhishID': phish_id,'PhishURL': phish_url,'Submitted': username, 'Valid': valid, 'Online': online})
        else:
            print("Failed to retrieve the page."+str(i))

            
            
