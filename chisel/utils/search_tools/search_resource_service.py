'''
File containing SearchResourceService that manages search resources
'''
from chisel.utils.search_tools.search_resources import GoogleNewsSearchResource, YahooSearchResource, AskRedditSearchResource, AskRedditSearchResource

class SearchResourceService:
    def get_resource(self, resource = "Yahoo", time_frame_days = 7):
        if(resource == "Yahoo"):
            return YahooSearchResource()
        if(resource == "Google"):
            return GoogleNewsSearchResource(time_frame_days)
        return AskRedditSearchResource()
         # add others... e.g. Bing 