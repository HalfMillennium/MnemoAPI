from ..search_resources import GoogleNewsSearchResource, YahooImagesSearchResource, AskRedditSearchResource
from ..utils import get_prior_and_current_date

EXAMPLE_PROMPT = "hello_world"

def test_google_search_resource():
    BASE_URL = GoogleNewsSearchResource.BASE_URL

    (seven_days_prior_date, current_date) = get_prior_and_current_date(7)
    expected_query = f'{BASE_URL}?q={EXAMPLE_PROMPT}&tbs=cdr:1,cd_min:{seven_days_prior_date},cd_max:{current_date}'

    google_search_resource = GoogleNewsSearchResource() # 7 is default window for time frame
    assert google_search_resource.build_query(EXAMPLE_PROMPT) == expected_query

    (four_days_prior_date, current_date) = get_prior_and_current_date(4)
    expected_query = f'{BASE_URL}?q={EXAMPLE_PROMPT}&tbs=cdr:1,cd_min:{four_days_prior_date},cd_max:{current_date}'

    google_search_resource = GoogleNewsSearchResource(4)
    assert google_search_resource.build_query(EXAMPLE_PROMPT) == expected_query

def test_yahoo_images_search_resource():
    BASE_URL = YahooImagesSearchResource.BASE_URL

    expected_query = f'{BASE_URL};?p={EXAMPLE_PROMPT}'

    yahoo_search_resource = YahooImagesSearchResource()
    assert yahoo_search_resource.build_query(EXAMPLE_PROMPT) == expected_query

def test_ask_reddit_search_resource():
    BASE_URL = AskRedditSearchResource.BASE_URL

    expected_query = f'{BASE_URL}?q={EXAMPLE_PROMPT}'

    ask_reddit_search_resource = AskRedditSearchResource()
    assert ask_reddit_search_resource.build_query(EXAMPLE_PROMPT) == expected_query

