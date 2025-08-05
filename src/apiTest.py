import os
import sys
import json
from pprint import pp
import genUtilities
from settings import *

session, csrf_token = genUtilities.create_wiki_session()
def test_api_connection(session, csrf_token):
    search_resp = session.get(api_url, params={
        "action": "query",
        "list": "search",
        "srsearch": "TestPagePleaseIgnore",
        "token": csrf_token,
        "format": "json"
    })

    search_data = search_resp.json()

    print(f"HTTP Status Code: {search_resp.status_code}")
    content_type = search_resp.headers.get("Content-Type", "")
    print(f"Content-Type: {content_type}")

    try:
        search_data = search_resp.json()
    except json.JSONDecodeError:
        print("Response is not valid JSON. Here’s the raw content:")
        print(response.text)
        return

    matches = search_data.get("query", {}).get("search", [])

    print(f"Search results for 'TestPagePleaseIgnore':")
    for match in matches:
        print(f" - {match['title']}")

test_api_connection(session, csrf_token)
