"""
Consider the url ‘http://www.immobiliare.it/Roma/agenzie_immobiliari_provincia-Roma.html’
Extract all inmobiliaries names published on first page.
"""

from loader import Loader

document = Loader('http://www.immobiliare.it/Roma/agenzie_immobiliari_provincia-Roma.html')
all_inmobiliaries = []


for h4 in document.soup.select("h4.titolo.text-primary"):
    all_inmobiliaries.append(h4.a.string)

if __name__ == '__main__':
    for title in all_inmobiliaries:
        print(title)
