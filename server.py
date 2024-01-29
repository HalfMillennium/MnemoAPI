'''
'grequests' performs necessary monkey-patching operations on server start-up, and should be the first module imported
'''
import grequests
import requests
import json
import asyncio
import uvicorn
from chisel.chiseler import fetch_page_text
from chisel.utils.search_tools.search_resource_service import SearchResourceService
from api.page_parser import PageParser
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

PORT = 8000

# Theoretically the prompt entered by a user would be the name of a public figure
@app.get("/thoughts/{name_prompt}")
async def get_thoughts(name_prompt, response_class=HTMLResponse):
    # chisel result is a list, so in case it returns multiple items (for some reason), join them with a page break
    query_generator = SearchResourceService().get_resource("Google", 3)
    page_text_request = fetch_page_text(query_generator.build_query(name_prompt))
    gathered_results = await asyncio.gather(page_text_request)
    page_html = gathered_results[0]
    parsed_page = PageParser(page_html)
    return HTMLResponse(content=page_html, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=PORT)