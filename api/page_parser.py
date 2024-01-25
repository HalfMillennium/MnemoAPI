from bs4 import BeautifulSoup
from markdownify import markdownify as md

class PageParser:
    def __init__(self, raw_html):
        self.page_soup = self.__make_soup(raw_html)
        self.raw_html = raw_html

    def __make_soup(self, raw_html):
        return BeautifulSoup(raw_html, 'html.parser')

    def get_links(self):
        for link in self.page_soup.find_all('a'):
            yield link.get('href')

    def get_paragraph_tags(self):
        for p in self.page_soup.find_all('p'):
            yield p.get_text()

    def get_markdown(self):
        return md(self.raw_html)
    
    def get_selector(self, selector, attr = None):
        for selector in self.page_soup.find_all(selector, attr):
            yield selector.getText()
        