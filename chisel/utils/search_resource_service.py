from chisel.utils.search_resources import GoogleSearchResource, YahooSearchResource

class SearchResourceService:
    def get_resource(self, resource = "Yahoo"):
        resource_map = {
            "Google": GoogleSearchResource,
            "Yahoo": YahooSearchResource,
            # add others... e.g. Bing 
        }
        return resource_map.get(resource)()