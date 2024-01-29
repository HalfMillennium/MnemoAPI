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

    def print_top_stories(self):
        # Find the "Top stories" section based on the heading text
        top_stories_heading = self.page_soup.find('div', text='Top stories')

        if top_stories_heading:
            # Navigate to the parent div of the heading to get the section
            top_stories_section = top_stories_heading.find_parent('div')

            if top_stories_section:
                # Extract information for each story
                stories = top_stories_section.find_all('a', href=True)

                for i, story in enumerate(stories, 1):
                    # Extract information from the HTML
                    title = story.find('span').text.strip() if story.find('span') else ''
                    source_posted = story.find_all('div')[-1].text.strip() if story.find_all('div') else ''

                    # Split source and posted information
                    source, posted = source_posted.split(maxsplit=1) if source_posted else ('', '')

                    # Create a dictionary
                    result_dict = {
                        'title': title,
                        'source': source,
                        'posted': posted
                    }
                    print(f'{result_dict}\n')
                            