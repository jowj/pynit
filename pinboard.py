import json
import os
import requests
import pysnooper


pinboard_token = os.environ.get("PINBOARD_TOKEN")
pinboard_base_url = "https://api.pinboard.in/v1/"

def get_all_posts():
    get_post_snippet = f"posts/all?auth_token={pinboard_token}"
    pinboard_url = pinboard_base_url + posts_url_snippet

    return requests.get(pinboard_url)
    
@pysnooper.snoop()
def add_pin_url(reddit_title, reddit_url, reddit_description, subreddit):
    add_post_snippet = f"posts/add?auth_token={pinboard_token}"
    args = {
        'url': reddit_url,
        'description': reddit_title,
        'extended': reddit_description,
        'tags': subreddit,
        'replace': no
    }
    pass
    
def import_reddit_url_from_file(filename):
    with open(filename, 'r') as infile:
        json.load(infile)

import_reddit_url_from_file("data.json")
