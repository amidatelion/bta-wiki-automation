import os
import sys
import requests

API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
ZONE_ID = "9ea05c324632c440cc68a3443c44c17b"
RULE_ID = "54f9f1389b994ebd932d9e8f8b54f63a"
FILTER_ID = "3f811b32e0a741cda562493a97c3afe1"
API_URL = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/firewall/rules/{RULE_ID}"

def toggle_firewall_rule(state):
    if state not in ("enable", "disable"):
        print("Usage: script.py [enable|disable]")
        sys.exit(1)

    paused = False if state == "enable" else True

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "id": RULE_ID,
        "paused": paused,
        "description": "API Skip",
        "action": "allow",
        "filter": {
            "id": FILTER_ID
        }
    }

    response = requests.put(API_URL, headers=headers, json=payload)
    data = response.json()

    if response.status_code == 200 and data.get("success"):
        print(f"Successfully {'enabled' if not paused else 'disabled'} the rule.")
    else:
        print("Failed to update rule.")
        print(data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py [enable|disable]")
        sys.exit(1)
    
    toggle_firewall_rule(sys.argv[1].lower())
