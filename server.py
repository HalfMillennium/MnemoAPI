'''
grequests performs necessary monkey-patching operations, and should be the first module imported
'''
import grequests
import requests
import json
import asyncio
from http.server import HTTPServer, BaseHTTPRequestHandler
from aiohttp import web
from chisel.chiseler import get_page_text
from chisel.utils.search_tools.search_resource_service import SearchResourceService
from api.page_parser import PageParser

async def handle(request):
    name_prompt = request.match_info.get('name_prompt')
    # chisel result is a list, so in case it returns multiple items (for some reason), join them with a page break
    query_generator = SearchResourceService().get_resource("Google", 7)
    gathered_results = await asyncio.gather(get_page_text(query_generator.build_query(name_prompt)))
    page_html = gathered_results[0]
    page_parser = PageParser(page_html)
    for result in page_parser.get_selector('span', {"class": "invisible"}):
        print(result)
    return web.Response(content_type="html", text=page_html)

async def run_web_server():
    app = web.Application()
    app.add_routes([web.get('/{name_prompt}', handle)])

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, 'localhost', PORT)
    await site.start()

    print(f'OmniScope service running on port {PORT}.')

if __name__ == "__main__":
    PORT = 8000 # local port for now
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_web_server())
    loop.run_forever()