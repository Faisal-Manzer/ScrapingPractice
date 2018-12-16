from bs4 import BeautifulSoup
from requests import request


class Loader:
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/71.0.3578.98 Safari/537.36 "

    def __init__(self, url, method="get", user_agent=False, parser="lxml", headers=None, console=True):

        if headers is None:
            headers = {}

        if user_agent:
            headers['user-agent'] = self.user_agent

        self.url = url
        self.method = method
        self.use_user_agent = user_agent

        self.html = request(method, url, headers=headers).text
        if console:
            print("Request Completed", url)

        self.soup = BeautifulSoup(self.html, parser)
        if console:
            print("Parser Completed\n")
