'''
File containing SearchResourceService that manages search resources
'''
from chisel.utils.search_tools.search_resources import GoogleNewsSearchResource, YahooImagesSearchResource, AskRedditSearchResource

class SearchResourceService:
    RESOURCES = {
        "Yahoo Images": YahooImagesSearchResource,
        "Google News": GoogleNewsSearchResource,
        "AskReddit": AskRedditSearchResource
        # TODO: Other resources necessary?
    }

    def __init__(self, resource = "Yahoo", time_frame_days = 7):
        self.resource = resource

    def build_query(self, prompt, time_frame_days = 7):
        current_resource = self.RESOURCES.get(self.resource)
        if(self.resource == "Google News"):
            # TODO: Allow other resources to accept time_frame_days argument
            return current_resource(time_frame_days).build_query(prompt)
        return current_resource().build_query(prompt)