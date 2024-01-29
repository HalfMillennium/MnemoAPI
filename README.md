# OmniScope 
## A Python service

_OmniScope_ is a python API that fetches real-world data about any given public figure, and researches a given public figure, views relevant current events involving them, then uses AI to generate a daily thought (that's hopefully humorous/entertaining)based on the public goings on of their lives.

This service leverages a Python library for grabbing snippets of search data (from several sources) and creating a first-person perspective based on current events (events pertaining to the figure) as well as historical information about the public figure (sourced from Wikipedia).

The service is created using FastAPI and will rely on a ChatGPT Python client to create the contextual thought.

OmniScope will be accessible via a React web front-end.
