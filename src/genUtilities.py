import os
import requests
import json
from settings import *

def create_wiki_session():

    username = os.getenv("WIKI_USER")
    password = os.getenv("WIKI_PASS")

    # Ensure username and password are set
    if not username or not password:
        raise ValueError("Username or password not found in environment variables.")

    # Initialize session
    session = requests.Session()

    # Step 1: Get an edit token
    login_token_resp = session.get(api_url, params={
        "action": "query",
        "meta": "tokens",
        "type": "login",
        "format": "json"
    })

    print(f"Status code: {login_token_resp.status_code}")
    print(f"Content-Type: {login_token_resp.headers.get('Content-Type')}")
    print("Raw response:")
    print(login_token_resp.text)

    login_token = login_token_resp.json()["query"]["tokens"]["logintoken"]

    # Step 2: Log in to the MediaWiki API
    login_resp = session.post(api_url, data={
        "action": "login",
        "lgname": username,
        "lgpassword": password,
        "lgtoken": login_token,
        "format": "json"
    })

    # Check if login was successful
    if login_resp.json().get("login", {}).get("result") != "Success":
        raise Exception("Login failed: " + str(login_resp.json()))

    # Step 3: Fetch the CSRF token for editing
    csrf_token_resp = session.get(api_url, params={
        "action": "query",
        "meta": "tokens",
        "format": "json"
    })
    csrf_token = csrf_token_resp.json()["query"]["tokens"]["csrftoken"]

    return session, csrf_token

def fetch_csrf_token(session):
    csrf_token_resp = session.get(api_url, params={
        "action": "query",
        "meta": "tokens",
        "format": "json"
    })
    return csrf_token_resp.json()["query"]["tokens"]["csrftoken"]

def post_to_wiki(session, csrf_token, page_title, page_content):
    # Step 4: Make the POST request to edit the page
    edit_resp = session.post(api_url, data={
        "action": "edit",
        "title": page_title,
        "text": page_content,
        "token": csrf_token,
        "format": "json"
    })

    # Check if the edit was successful
    if edit_resp.json().get("edit", {}).get("result") == "Success":
        return True
    elif edit_resp.json().get("error", {}).get("code") == "badtoken":
        print("Invalid CSRF token. Refreshing and retrying once...")

        csrf_token = fetch_csrf_token(session)
        edit_resp = session.post(api_url, data={
            "action": "edit",
            "title": page_title,
            "text": page_content,
            "token": csrf_token,
            "format": "json"
        })

        if edit_resp.json().get("edit", {}).get("result") == "Success":
            return True
        else:
            print(f"Failed to edit page '{page_title}':", edit_resp.json())
            return False
    else:
        print(f"Failed to edit page '{page_title}':", edit_resp.json())
        return False

    
def index_csv_files(directories):
    csv_files = {}
    # Walk through directories recursively
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                # Check if the file ends with .csv
                if file.endswith('.csv'):
                    file_name = file[:-4]
                    full_path = os.path.join(root, file)
                    # Add the file path to the list for this file name
                    if file_name in csv_files:
                        csv_files[file_name].append(full_path)
                    else:
                        csv_files[file_name] = [full_path]
    return csv_files


def get_display_name(item):
    for root, dirs, files in os.walk(bta_dir):
        for file in files:
            # Check if the file is the target JSON file
            if file == item+".json":
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    # Use UIName if available, otherwise use Name because fucking vehicledefs
                    ui_name = data['Description'].get('UIName', data['Description'].get('Name'))
                    return ui_name