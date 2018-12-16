"""
Consider the url ‘http://www.gibbon.se/Retailer/Map.aspx?SectionId=832’.
Extract the links to the detailed information of each row on the table.
For example, for the first adress, Karlbergsvägen 32, 113 27 stockholm, the details are
A.E.N HUND I STAN AB
ADRESS OCH ÖPPETTIDER
Karlbergsvägen 32
113 27 STOCKHOLM
Öppettider:
Telefon: 08-313058
Mail-adress: info@hundistan.eu
Hemsida:
The link to that details (clicking on Karlbergsvägen 32, 113 27 stockholm) is http://www.gibbon.se/Retailer/Retailer.aspx?ItemId=45128.
You have to extract all the links available, one per row.
"""

from loader import Loader
from re import match

document = Loader('http://www.gibbon.se/Retailer/Map.aspx?SectionId=832')
links = set()


for link in document.soup.select('table.storelist a'):
    href = link['href']
    m = match(r'Retailer\.aspx\?ItemId=(?P<id>[0-9]+)', href)

    if m and m.group('id'):
        links.add('http://www.gibbon.se/Retailer/Retailer.aspx?ItemId=' + m.group('id'))

if __name__ == '__main__':
    for link in links:
        print(link)
