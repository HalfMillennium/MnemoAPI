'''
File containing SearchResourceService that manages search resources
'''
from chisel.utils.search_tools.search_resources import GoogleSearchResource, YahooSearchResource, AskRedditSearchResource, AskRedditSearchResource

class SearchResourceService:
    def get_resource(self, resource = "Yahoo"):
        resource_map = {
            "Google": GoogleSearchResource,
            "Yahoo": YahooSearchResource,
            "AskReddit": AskRedditSearchResource,
            # add others... e.g. Bing 
        }
        return resource_map.get(resource)()