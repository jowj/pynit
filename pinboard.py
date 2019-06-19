import requests
import os
import pysnooper

pinboard_token = os.environ.get("PINBOARD_TOKEN")
pinboard_base_url = "https://api.pinboard.in/v1/"

def get_all_posts():
    posts = f"posts/all?auth_token={pinboard_token}"
    pinboard_url = pinboard_base_url + posts

    return requests.get(pinboard_url)
    
