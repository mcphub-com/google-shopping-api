import os
import requests
from typing import Union, Annotated, Literal
from pydantic import Field
from mcp.server import FastMCP
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP('serp-shopping-search')

serp_url = "https://serpapi.com/search"
serp_api_key = os.getenv("SERP_API_KEY")


@mcp.tool()
def search_google_shopping(
    q: Annotated[Union[str, None], Field(
        description="Required. Parameter defines the query you want to search. You can use anything that you would use in a regular Google Shopping search."
    )] = None,

    location: Annotated[Union[str, None], Field(description="Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The location and uule parameters can't be used together. It is recommended to specify location at the city level in order to simulate a real user’s search. If location is omitted, the search may take on the location of the proxy.")] = None,

    tbs: Annotated[Union[str, None], Field(
        description="Optional. Defines advanced search parameters not possible in regular queries."
    )] = None,

    shoprs: Annotated[Union[str, None], Field(
        description="Optional. Helper ID for setting search filters. Must be used with updated q parameter containing filter names."
    )] = None,

    direct_link: Annotated[Union[bool, None], Field(
        description="Optional. When true, attempts to include direct product links (may increase search time). Only applies to new layout countries."
    )] = None,

    start: Annotated[Union[int, None], Field(
        description="Optional. Result offset for pagination (e.g., 0=first page, 60=second page). Not recommended for new layout."
    )] = None,

    num: Annotated[Union[int, None], Field(
        description="Optional. Maximum results to return (1-100, default=60). Not supported in new layout."
    )] = None,

    device: Annotated[Union[Literal["desktop", "tablet", "mobile"], None], Field(
        description="Optional. Device type for results: desktop (default), tablet, or mobile."
    )] = None,

    no_cache: Annotated[Union[bool, None], Field(
        description="Optional. When true, forces fresh results ignoring cached versions. Cannot be used with async."
    )] = None,

    aasync: Annotated[Union[bool, None], Field(
        description="Optional. When true, submits search asynchronously. Cannot be used with no_cache or Ludicrous Speed accounts."
    )] = None,

    zero_trace: Annotated[Union[bool, None], Field(
        description="Optional. Enterprise only. When true, enables ZeroTrace mode (no server storage)."
    )] = None,
):
    """Search Google Shopping for product listings and shopping results"""
    if location:
        q = q + ", location: %s"%location

    payload = {
        'engine': "google_shopping",
        'api_key': serp_api_key,
        'q': q,
        'tbs': tbs,
        'shoprs': shoprs,
        'direct_link': direct_link,
        'start': start,
        'num': num,
        'device': device,
        'no_cache': no_cache,
        'async': aasync,
        'zero_trace': zero_trace,
    }
    # Remove None values
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(serp_url, params=payload)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    mcp.run(transport="stdio")