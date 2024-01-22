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
    name_prompt = request.match_info.get('name_prompt')
    # chisel result is a list, so in case it returns multiple items (for some reason), join them with a page break
    query_generator = SearchResourceService().get_resource("AskReddit")
    page_html = '<br></br>'.join(
        await asyncio.gather(
            get_page_text(query_generator.build_query(name_prompt))
        )
    )
    page_parser = PageParser(page_html)
    return web.Response(text=page_html)

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