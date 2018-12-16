"""
Consider the url ‘http://r-exercises.com/start-here-to-learn-r/’
Extract all the topics available on the url.
"""

from loader import Loader
# noinspection PyProtectedMember
from bs4 import Tag

document = Loader('http://r-exercises.com/start-here-to-learn-r/', user_agent=True)
topics = {}

for topic in document.soup.select('p > strong'):
    sub_topics = []

    ol = topic.parent.next_sibling

    while type(ol) != Tag:
        ol = ol.next_sibling

    if ol.name == "ol":
        for li in ol:
            sub_topic = li.string
            if sub_topic != '\n' and sub_topic:
                sub_topics.append(sub_topic.strip())

        topics[topic.text.strip()] = sub_topics

if __name__ == '__main__':
    for topic in topics:
        print(topic, ":", sep="")

        for sub_topic in topics[topic]:
            print(" "*5, sub_topic)

        print()
