'''
File containing all SearchResource classes
'''
from datetime import datetime, timedelta
from ...utils.search_tools.types.search_resource import SearchResource
from .utils import get_prior_and_current_date

class GoogleNewsSearchResource(SearchResource):
    BASE_URL = "https://news.google.com/search"
    SOURCE_NAME = "Google News Search"

    def __init__(self, time_frame_days = 7):
        (self.earliest_date, self.current_date) = get_prior_and_current_date(time_frame_days)

    def build_query(self, prompt):
        query = f'{self.BASE_URL}?q={prompt}&tbs=cdr:1,cd_min:{self.earliest_date},cd_max:{self.current_date}'
        print(f'BUILT [{self.SOURCE_NAME}] QUERY: "{query}"')
        return query
        
    def get_name(self):
        return self.SOURCE_NAME

    def parse_page_stories(raw_html):
        pass

class YahooSearchResource(SearchResource):
    BASE_URL = "https://search.yahoo.com/search"
    SOURCE_NAME = "Yahoo Search"

    def build_query(self, prompt):
        query = f'{self.BASE_URL}?q={prompt}'
        print(f'BUILT [{self.SOURCE_NAME}] QUERY: "{query}"')
        return query
        
    def get_name(self):
        return self.SOURCE_NAME

class AskRedditSearchResource(SearchResource):
    BASE_URL = "https://www.reddit.com/r/AskReddit/search"
    SOURCE_NAME = "Reddit Search"

    def __init__(self, sort = "hot"):
        self.sort = sort

    def build_query(self, prompt):
        query = f'{self.BASE_URL}?q={prompt}'
        print(f'BUILT [{self.SOURCE_NAME}] QUERY: "{query}"')
        return query
        
    def get_name(self):
        return self.SOURCE_NAME