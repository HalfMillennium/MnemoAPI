'''
Interface for SearchResource object
'''
class SearchResource:
    def build_query(self, query: str) -> str:
        """Return full query url using base URL and input query arg."""
        pass

    def get_name(self) -> str:
        """Return name of source, e.g. "Bing Search"."""
        pass