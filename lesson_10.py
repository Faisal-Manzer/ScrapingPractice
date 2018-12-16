"""
Consider the url ‘http://www.gibbon.se/Retailer/Map.aspx?SectionId=832’.
Build a data frame with all the information available for each row.
For example, for the first adress, Karlbergsvägen 32, 113 27 stockholm, the details are
A.E.N HUND I STAN AB

ADRESS OCH ÖPPETTIDER
Karlbergsvägen 32
113 27 STOCKHOLM
Öppettider:
Telefon: 08-313058
Mail-adress: info@hundistan.eu
Hemsida:
For the second row, Inedalsgatan 5, 112 33 stockholm, the details are
ARKENZOO KUNGSHOLMEN A
ADRESS OCH ÖPPETTIDER
Kungs Zoo AB
Inedalsgatan 5
112 33 STOCKHOLM
Öppettider:
Telefon: 08-7248110
Mail-adress: kungsholmen@arkenzoo.se
Hemsida: www.arkenzoo.se

This details will be saved on the first row of the data.frame.
Website address Name of store Phone Number Email adress City Country
1 A.E.N Hund i Stan AB 08-313058 info@hundistan.eu Stocholm Sweden
2 www.arkenzoo.se ArkenZoo Kungsholmen A 08-7248110 kungsholmen@arkenzoo.se Stocholm Sweden
"""

from loader import Loader
# noinspection PyProtectedMember
from bs4 import NavigableString
from lesson_6 import links

# main_document = Loader(link, console=False)
stores = []

details = ['OpeningHours', 'Phone', 'Email', 'Website']


class Store:
    def __init__(self, doc):
        spans = doc.soup.select('.width100', limit=4)
        h1 = doc.soup.select('h1', limit=2)[1]

        parent = spans[0].parent

        self.details = dict()
        self.title = h1.text

        address = ''
        for line in parent.span.children:
            if type(line) == NavigableString:
                address += line.string.strip() + ', '

        if address != '':
            self.details['address'] = address[:-2].strip()

        for i in range(len(details)):
            self.details[details[i]] = spans[i].next_sibling.next_sibling.text.strip()

    def __str__(self):
        detail = self.title.title()
        for key in self.details:
            detail += '\n' + key.title() + ': ' + self.details[key]

        return detail


for link in links:
    store = Store(Loader(link, console=False))

    if __name__ == '__main__':
        print(store, '\n')

    stores.append(store)
