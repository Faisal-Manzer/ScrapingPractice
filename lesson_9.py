"""
Consider the url=’http://www.dictionary.com/browse/’ and the words ‘handy’,’whisper’,’lovely’,’scrape’.
Build a data frame, where the first variables is “Word” and the second variables is “definitions”. Scrape the definitions
from the url.
"""

from loader import Loader

words = ('handy', 'whisper', 'lovely', 'scrape', )

for word in words:
    document = Loader('http://www.dictionary.com/browse/' + word)

# NOT COMPLETED YET
