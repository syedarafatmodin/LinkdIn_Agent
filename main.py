import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import Tool
from dotenv import load_dotenv

load_dotenv()

from langchain_tavily import TavilySearch

tool = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None
)

