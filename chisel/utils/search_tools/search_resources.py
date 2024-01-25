'''
File containing all SearchResource classes
'''
from chisel.utils.search_tools.types.search_resource import SearchResource
from datetime import datetime, timedelta

class GoogleSearchResource(SearchResource):
    BASE_URL = "https://www.google.com/search"
    SOURCE_NAME = "Google Search"

    def __init__(self, time_frame_days = 7):
        # total length of date range
        self.time_frame_days = time_frame_days

        # get the current date in MM/DD/YYYY format
        self.current_date = datetime.now().strftime("%m/%d/%Y")

        # ...earliest result will be {TIME_FRAME_DAYS} days ago
        self.earliest_date = (datetime.now() - timedelta(days=self.time_frame_days)).strftime("%m/%d/%Y")

    def build_query(self, query):
        query = f'{self.BASE_URL}?q={query}&tbs=cdr:1,cd_min:{self.earliest_date},cd_max:{self.current_date}'
        print(f'Built query: {query}')
        return query
        
    def get_name(self):
        return self.SOURCE_NAME

class YahooSearchResource(SearchResource):
    BASE_URL = "https://search.yahoo.com/search"
    SOURCE_NAME = "Yahoo Search"

    def build_query(self, query):
        return f'{self.BASE_URL}?q={query}'
        
    def get_name(self):
        return self.SOURCE_NAME

class AskRedditSearchResource(SearchResource):
    BASE_URL = "https://www.reddit.com/r/AskReddit/search"
    SOURCE_NAME = "Reddit Search"

    def __init__(self, sort = "hot"):
        self.sort = sort

    def build_query(self, query):
        return f'{self.BASE_URL}?q={query}&sort={self.sort}'
        
    def get_name(self):
        return self.SOURCE_NAME