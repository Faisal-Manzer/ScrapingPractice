"""
Consider the url ‘http://www2.sas.com/proceedings/sugi30/toc.html’
Extract all the papers names, from 001-30 to 268-30
"""

from loader import Loader


class Paper:
    def __init__(self, paragraph):

        try:
            self.number = paragraph.b.a.text
            self.name = paragraph.cite.text
            self.author = list(paragraph.children)[2]

            self.correct = True
        except AttributeError:
            self.correct = False

    def __str__(self):
        return "{} => '{}' by {}".format(self.number, self.name, self.author)


document = Loader('http://www2.sas.com/proceedings/sugi30/toc.html', parser="html.parser")
all_papers = []


for cite in document.soup.find_all('cite'):
    try:
        para = cite.parent.parent
    except AttributeError:
        continue

    if para.name == "p":
        paper = Paper(para)
        if paper.correct:
            all_papers.append(paper)

if __name__ == '__main__':
    for paper in all_papers:
        print(paper)
