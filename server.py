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
from chisel.page_parser.page_parser_service import PageParserService
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

PORT = 8000

'''
Return AI generated diary entry based on the current events related to the search term name_prompt
'''
@app.get("/diary_entry/{name_prompt}")
async def get_diary_entry(name_prompt, response_class=HTMLResponse):
    # TODO: Replace individual resource name and time_frame_days arguments to single 'ResourceSpec' object 
    # that includes optional field 'time_frame_days' and required field 'resource_name'
    query_generator = SearchResourceService("Yahoo Images")
    page_text_request = fetch_page_text(query_generator.build_query(name_prompt))
    gathered_results = await asyncio.gather(page_text_request)

    # TODO: Either parse more than just the first entry from gathered_results or do not return full array from page_text_request
    page_html = gathered_results[0]

    # TODO: Instead of printing results, return as proper JSONResponse
    __print_stories(page_html)
    return HTMLResponse(content=page_html, status_code=200)

'''
Returns a set of relevant images related to the search term name_prompt
'''
@app.get("/images/{name_prompt}")
async def get_images(name_prompt, response_class=JSONResponse):
    # TODO: Replace individual resource name and time_frame_days arguments to single 'ResourceSpec' object 
    # that includes optional field 'time_frame_days' and required field 'resource_name'
    query_generator = SearchResourceService("Yahoo Images")
    page_text_request = fetch_page_text(query_generator.build_query(name_prompt))
    gathered_results = await asyncio.gather(page_text_request)

    # TODO: Either parse more than just the first entry from gathered_results or do not return full array from page_text_request
    page_html = gathered_results[0]

    images = list(__fetch_images(page_html, name_prompt))
    return JSONResponse(content={'data': images }, status_code=200)

def __print_stories(html_content):
    google_news_page_parser = PageParserService("Google News", html_content)
    articles = google_news_page_parser.get_stories() # { title: string, source: string, date_posted: string }[]
    for i, article in enumerate(articles, 1):
        print(f'{article["title"]}, posted {article["posted_time_ago"]}\n')

def __fetch_images(html_content, alt = None):
    yahoo_images_parser = PageParserService("Yahoo Images", html_content)
    images = yahoo_images_parser.get_images(alt) # { src: string, alt: string | None }[]
    return images

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=PORT)