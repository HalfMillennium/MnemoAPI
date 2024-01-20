'''
File containing all SearchResource classes
'''
from chisel.utils.types.search_resource import SearchResource

class GoogleSearchResource(SearchResource):
    BASE_URL = "https://www.google.com/search"
    SOURCE_NAME = "Google Search"

    def build_query(self, query):
        return f'{self.BASE_URL}?q={query}'
        
    def get_name(self):
        return self.SOURCE_NAME

class YahooSearchResource(SearchResource):
    BASE_URL = "https://search.yahoo.com/search"
    SOURCE_NAME = "Yahoo Search"

    def build_query(self, query):
        return f'{self.BASE_URL}?q={query}'
        
    def get_name(self):
        return self.SOURCE_NAME