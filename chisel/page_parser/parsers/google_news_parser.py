'''
Parsing library for Google News search results
'''
from bs4 import BeautifulSoup
from ...utils.search_tools.types.page_parser import PageParser

class GoogleNewsParser(PageParser):
    def __init__(self, raw_html):
        self.page_soup = self.__make_soup(raw_html)
        self.raw_html = raw_html

    def __make_soup(self, raw_html):
        return BeautifulSoup(raw_html, 'html.parser')

    def __fetch_story_details(self, article_element):
        sub_contents = article_element

        title_element = sub_contents.find('a', attrs={"data-n-tid": "29"})
        title = title_element.text if title_element else None
        
        time_posted_element = sub_contents.find('time')  # Assuming the posted time is within a time tag
        time_posted = time_posted_element.text if time_posted_element else ''

        source_element = sub_contents.find('div', attrs={"data-n-tid": "9"})
        source = source_element.text if source_element else None
        
        return {'title': title, 'source': source, 'time_posted': time_posted}

    def get_paragraphs(self):
        for p in self.page_soup.find_all('p'):
            yield p.get_text()

    # TODO: Implement get_images_from_page(count):

    def get_stories(self):
        article_elements = self.page_soup.find_all('article')

        for element in article_elements:
            element_details = self.__fetch_story_details(element)
            yield element_details
                        