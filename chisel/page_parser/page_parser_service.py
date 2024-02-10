from .parsers.google_news_parser import GoogleNewsParser

class PageParserService:
    PARSERS = {
        "Google News": GoogleNewsParser
        # Create and add others
    }

    def __init__(self, resource, raw_html):
        self.resource = resource
        self.raw_html = raw_html
        self.parser = self.PARSERS.get(self.resource)(self.raw_html)
    
    def get_paragraphs(self):
        return self.parser.get_paragraph_tags(self.raw_html)

    def get_stories(self):
        return self.parser.get_stories()
    