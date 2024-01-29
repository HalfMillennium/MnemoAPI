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

# The prompt entered by a user should be the name of a public figure
@app.get("/thoughts/{name_prompt}")
async def get_thoughts(name_prompt, response_class=HTMLResponse):
    # TODO: Replace individual resource name and time_frame_days arguments to single 'ResourceSpec' object 
    # that includes optional field 'time_frame_days' and required field 'resource_name'
    query_generator = SearchResourceService("Google News", 3)
    page_text_request = fetch_page_text(query_generator.build_query(name_prompt))
    gathered_results = await asyncio.gather(page_text_request)

    # TODO: Parse more than just the first entry from gathered_results
    page_html = gathered_results[0]
    parsed_page = PageParser(page_html)
    return HTMLResponse(content=page_html, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=PORT)