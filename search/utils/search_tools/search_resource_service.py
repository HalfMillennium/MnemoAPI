'''
File containing SearchResourceService that manages search resources and conducts page fetching.
'''
import grequests
import asyncio
from search.utils.search_tools.search_resources import GoogleNewsSearchResource, YahooImagesSearchResource, AskRedditSearchResource
from ...page_parser.page_parser_service import PageParserService

class SearchResourceService:
    RESOURCES = {
        "Yahoo Images": YahooImagesSearchResource,
        "Google News": GoogleNewsSearchResource,
        "AskReddit": AskRedditSearchResource
        # TODO: Other resources necessary?
    }

    def __init__(self, resource_name = "Yahoo Images", time_frame_days = 7):
        self.resource_name = resource_name
        self.time_frame_days = time_frame_days
        if(self.resource_name == "Google News"):
            # TODO: Allow other resources to accept time_frame_days argument
            self.current_resource = self.RESOURCES.get(self.resource_name)(time_frame_days)
        else:
            self.current_resource = self.RESOURCES.get(self.resource_name)()

    def build_query(self, prompt) -> str:
        return self.current_resource.build_query(prompt)

    async def execute_query(self, search_term) -> str:
        query_details = self.build_query(search_term)
        result = await self.__fetch_page_content(query_details)
        return result

    async def __fetch_page_content(self, url) -> str:
        # Create a list of URLs to request asynchronously
        urls = [url]
        # Use grequests.map to perform the asynchronous request
        response = grequests.map((grequests.get(u) for u in urls))
        return self.parse_response(response)

    async def fetch_and_parse_images(self, search_term, alt = None, resource_name = "Yahoo Images"):
        page_html = await self.execute_query(search_term)
        yahoo_images_parser = PageParserService(resource_name, page_html)
        images = yahoo_images_parser.get_images(alt) # { src: string, alt: string | None }[]
        return images

    '''
    Exposed for testing, should not be used directly
    '''
    def parse_response(self, responses):
        if responses == []:
            return None
        return responses[0].text if responses[0] else None