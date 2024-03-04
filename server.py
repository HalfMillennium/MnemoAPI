'''
'grequests' performs necessary monkey-patching operations on server start-up, and should be the first module imported
'''
import grequests
import requests
import json
import asyncio
import uvicorn
from search.utils.search_tools.search_resource_service import SearchResourceService
from search.page_parser.page_parser_service import PageParserService
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

PORT = 8000

'''
Return AI generated first-person POV diary entry based on the current events related to the search term name_prompt
'''
@app.get("/diary_entry/{name_prompt}")
async def get_diary_entry(name_prompt, response_class=HTMLResponse):
    # TODO: Replace individual resource name and time_frame_days arguments to single 'ResourceSpec' object 
    # that includes optional field 'time_frame_days' and required field 'resource_name'
    google_news_search = SearchResourceService("Google News")
    page_html = await google_news_search.execute_query(name_prompt)

    return HTMLResponse(content=page_html, status_code=200)

'''
Returns a set of relevant images related to the search term name_prompt
'''
@app.get("/images/{name_prompt}")
async def get_images(name_prompt, response_class=JSONResponse):
    yahoo_images_search = SearchResourceService("Yahoo Images")
    images = await asyncio.gather(yahoo_images_search.fetch_and_parse_images(name_prompt))
    
    return JSONResponse(content=list(images[0]), status_code=200)

def print_google_news_stories(html_content):
    google_news_page_parser = PageParserService("Google News", html_content)
    articles = google_news_page_parser.get_stories() # { title: string, source: string, date_posted: string }[]
    for i, article in enumerate(articles, 1):
        print(f'{article["title"]}, posted {article["posted_time_ago"]}\n')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=PORT)