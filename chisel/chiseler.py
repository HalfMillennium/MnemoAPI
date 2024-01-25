import grequests
import asyncio


async def get_page_text(url):
    # Create a list of URLs to request asynchronously
    urls = [url]

    # Use grequests.map to perform the asynchronous request
    responses = grequests.map((grequests.get(u) for u in urls))

    # Return the response
    return responses[0].text if responses[0] else None