from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import requests
import asyncio
from aiohttp import web
from chisel.chisel import get_page_text
from bs4 import BeautifulSoup
from chisel.utils.search_resource_service import SearchResourceService

PORT = 8000

async def handle(request):
    name_prompt = request.match_info.get('name_prompt')
    # chisel result is a list, so in case it returns multiple items for some reason (?) join them with a page break
    query_generator = SearchResourceService().get_resource()
    page_text = '<br></br>'.join(await asyncio.gather(get_page_text(query_generator.build_query(name_prompt))))
    return web.Response(content_type="html",text=page_text)

async def run_web_server():
    app = web.Application()
    app.add_routes([web.get('/{name_prompt}', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', PORT)
    await site.start()
    print(f'Omni service running on port {PORT}')

loop = asyncio.get_event_loop()
loop.create_task(run_web_server())
loop.run_forever()