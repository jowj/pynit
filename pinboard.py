import json
import os
import requests
import pysnooper


pinboard_token = os.environ.get("PINBOARD_TOKEN")
pinboard_base_url = "https://api.pinboard.in/v1/"

def get_all_posts():
    get_post_snippet = f"posts/all?auth_token={pinboard_token}"
    pinboard_url = pinboard_base_url + get_post_snippet

    return requests.get(pinboard_url)
    

def add_pin_url(reddit_dict):
    add_post_snippet = f"posts/add?auth_token={pinboard_token}"
    headers = {'Content-type': 'application/json'}
    args = {
        'url': reddit_dict.url,
        'description': reddit_dict.title,
        'extended': reddit_dict.description,
        'tags': reddit_dict.tag,
        'replace': no
    }

    post_url = pinboard_base_url + add_post_snippet
    args_json = json.dumps(args)
    response = requests.post(post_url, data=args_json, headers=headers)
    return response

@pysnooper.snoop()
def import_reddit_url_from_file(filename):
    with open(filename, 'r') as infile:
        data = json.loads(infile.read())
    return data


if __name__ == "__main__":
    dict = import_reddit_url_from_file("data.json")
    add_pin_url(dict)
