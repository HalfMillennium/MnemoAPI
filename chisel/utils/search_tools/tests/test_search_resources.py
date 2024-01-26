import sys
sys.path.append('../')

from search_resources import GoogleSearchResource, YahooSearchResource, AskRedditSearchResource
from chisel.search_tools.utils import get_prior_and_current_date

EXAMPLE_PROMPT = "hello_world"

def test_google_search_resource():
    (seven_days_prior_date, current_date) = get_prior_and_current_date(7)
    expected_query = f'{self.BASE_URL}?q={prompt}&tbs=cdr:1,cd_min:{seven_days_prior_date},cd_max:{current_date}'

    google_search_resource = GoogleSearchResource() # 7 is default window for time frame
    assert google_search_resource.build_query(EXAMPLE_PROMPT) == expected_query

    (four_days_prior_date, current_date) = get_current_and_prior_date(4)
    expected_query = f'{self.BASE_URL}?q={prompt}&tbs=cdr:1,cd_min:{four_days_prior},cd_max:{current_date}'

    google_search_resource = GoogleSearchResource(4)
    assert google_search_resource.build_query(EXAMPLE_PROMPT) == expected_query