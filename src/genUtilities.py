import os
import requests
import json

codebase_dir = "/home/runner/work/BattleTech-Advanced/BattleTech-Advanced/bta"
#codebase_dir = "../../BattleTech-Advanced/"

# deeply ugly login function
def post_to_wiki(page_title, page_content):
    """
    Posts content to a specified page on a MediaWiki site.

    Parameters:
        page_title (str): The title of the MediaWiki page to edit or create.
        page_content (str): The content to post to the page.

    Returns:
        bool: True if the page was successfully posted, False otherwise.
    """
    # Load credentials from environment variables
    username = os.getenv("WIKI_USER")
    password = os.getenv("WIKI_PASS")

    # Define the MediaWiki API endpoint
    api_url = "https://www.bta3062.com/api.php"

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
        print("Login failed:", login_resp.json())
        return False

    # Step 3: Fetch the CSRF token for editing
    csrf_token_resp = session.get(api_url, params={
        "action": "query",
        "meta": "tokens",
        "format": "json"
    })
    csrf_token = csrf_token_resp.json()["query"]["tokens"]["csrftoken"]

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
        print(f"... successfully posted to '{page_title}' on the MediaWiki")
        return True
    else:
        print("Failed to edit page:", edit_resp.json())
        return False
    
def index_csv_files(directories):
    csv_files = {}
    
    # Walk through directories recursively
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                # Check if the file ends with .csv
                if file.endswith('.csv'):
                    # Append the full file path to the list
                    csv_files[file[:-4]]=os.path.join(root, file)
    
    return csv_files


def get_display_name(item):
    for root, dirs, files in os.walk(codebase_dir):
        for file in files:
            # Check if the file is the target JSON file
            if file == item+".json":
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    # Use UIName if available, otherwise use Name because fucking vehicledefs
                    ui_name = data['Description'].get('UIName', data['Description'].get('Name'))
                    return ui_name