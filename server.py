import json
import requests
import asyncio
from http.server import HTTPServer, BaseHTTPRequestHandler
from aiohttp import web
from chisel.chiseler import get_page_text
from chisel.utils.search_tools.search_resource_service import SearchResourceService
from api.page_parser import PageParser

# local port
PORT = 8000

async def handle(request):
    sentiment_base_url = "https://twitter.com"
    name = request.match_info.get('name_prompt')
    prompt = f'{name} {sentiment_base_url}'
    # chisel result is a list, so in case it returns multiple items (for some reason), join them with a page break
    query_generator = SearchResourceService().get_resource("Google")
    page_html = '<br></br>'.join(
        await asyncio.gather(
            get_page_text(query_generator.build_query(prompt))
        )
    )
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
    print(f'Omni service running on port {PORT}.')

loop = asyncio.get_event_loop()
loop.create_task(run_web_server())
loop.run_forever()