import requests
import os

pinboard_token = os.environ.get("PINBOARD_TOKEN")
pinboard_user = os.environ.get("PINBOARD_USER")
pinboard_password = os.environ.get("PINBOARD_PASSWORDD")
pinboard_url = f"https://{pinboard_user}:{pinboard_password}api.pinboard.in/v1"

requests.get(pinboard_url)

