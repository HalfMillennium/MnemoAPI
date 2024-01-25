import grequests
import asyncio

async def fetch_page_text(url):
    # Create a list of URLs to request asynchronously
    urls = [url]
    # Use grequests.map to perform the asynchronous request
    response = grequests.map((grequests.get(u) for u in urls))
    return parse_response(response)

def parse_response(responses):
    return responses[0].text if responses[0] else None