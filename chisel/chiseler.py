import requests
import asyncio


async def get_page_text(url):
    page_text = ''
    try:
        page = requests.get(url)
        page_text = page.text
    except:
        raise('CHISEL ERROR: Error fetching page text...')
    return page_text