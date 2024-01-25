'''
File containing all SearchResource classes
'''
from chisel.utils.search_tools.types.search_resource import SearchResource

class GoogleSearchResource(SearchResource):
    BASE_URL = "https://www.google.com/search"
    SOURCE_NAME = "Google Search"
    TIME_FRAME_DAYS = 7 # total length of date range

    # Get the current date in MM/DD/YYYY format
    current_date = datetime.now().strftime("%m/%d/%Y")

    # ...earliest result will be {TIME_FRAME_DAYS} days ago
    earliest_date = (datetime.now() - timedelta(days=7)).strftime("%m/%d/%Y")

    def build_query(self, query):
        return f'{self.BASE_URL}?q={query}&tbs=cdr:1,cd_min:{earliest_date},cd_max:{current_date}'
        
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