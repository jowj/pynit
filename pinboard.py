import json
import os
import time
import requests


PINBOARD_TOKEN = os.environ.get("PINBOARD_TOKEN")
PINBOARD_BASE_URL = "https://api.pinboard.in/v1/"
PINBOARD_AUTH_SNIPPET = f"?auth_token={PINBOARD_TOKEN}"

def get_all_posts():
    """
    returns a list of all pins in pinboard account
    """
    get_post_snippet = f"posts/all?auth_token={PINBOARD_TOKEN}"
    pinboard_url = PINBOARD_BASE_URL + get_post_snippet

    return requests.get(pinboard_url)


def add_pin_url(reddit_dict):
    """
    adds a pin to pinboard and returns the response
    """
    add_post_snippet = "posts/add"
    # headers = {'Content-type': 'application/json'}
    args = {
        'url': reddit_dict['url'],
        'description': reddit_dict['title'],
        'extended': reddit_dict['description'],
        'tags': reddit_dict['tag'],
        'replace': 'no'
    }

    post_url = PINBOARD_BASE_URL + add_post_snippet + PINBOARD_AUTH_SNIPPET

    response = requests.get(post_url, params=args)
    # pdb.set_trace()
    print(response.text)
    return response


def import_reddit_url_from_file(filename):
    """
    imports a list of reddit URLs and meta data from a file. 
    returns a json object of that data.
    """
    with open(filename, 'r') as infile:
        data = json.loads(infile.read())

    return data


if __name__ == "__main__":
    """
    You have to sleep for 3 seconds between requests or Maciej will Get Unhappy
    per https://pinboard.in/api
    """
    REDDIT_DATA = import_reddit_url_from_file("data.json")
    for entry in REDDIT_DATA:
        post_response = add_pin_url(entry)
        time.sleep(3)
