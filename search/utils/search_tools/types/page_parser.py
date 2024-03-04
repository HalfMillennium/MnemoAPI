'''
Interface for PageParser object
'''
from pydantic import BaseModel

class StoryResult(BaseModel):
    title: str
    source: str | None = None
    date_posted: str | None = None

class PageParser:
    def get_paragraphs(self, query: str) -> str:
        """Return all paragraph elements (<p>) on the page"""
        pass

    def get_stories(self) -> [StoryResult]:
        """Retrieve all news events/stories listed on the page"""
        pass
    
    # TODO: Add more parsing options