"""
Consider the url ‘http://www.gibbon.se/Retailer/Map.aspx?SectionId=832’
Extract all the options (countries) availables on select button.
"""

from loader import Loader

document = Loader("http://www.gibbon.se/Retailer/Map.aspx?SectionId=832")
countries = []


class Country:
    def __init__(self, option):
        try:
            self.name = option.text
            self.code = option['value']

            self.correct = True
        except AttributeError:
            self.correct = False

    def __str__(self):
        return "{} ({})".format(self.name, self.code)


for opt in document.soup.select("#ctl00_ContentPlaceHolder1__countries > option"):
    country = Country(opt)

    if country.correct:
        countries.append(country)

if __name__ == '__main__':
    for country in countries:
        print(country)
