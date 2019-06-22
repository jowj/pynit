import json
import os
import requests
import time


pinboard_token = os.environ.get("PINBOARD_TOKEN")
pinboard_base_url = "https://api.pinboard.in/v1/"
pinboard_auth_snippet = f"?auth_token={pinboard_token}"

def get_all_posts():
    get_post_snippet = f"posts/all?auth_token={pinboard_token}"
    pinboard_url = pinboard_base_url + get_post_snippet

    return requests.get(pinboard_url)
    

def add_pin_url(reddit_dict):
    add_post_snippet = "posts/add"
    # headers = {'Content-type': 'application/json'}
    args = {
        'url': reddit_dict['url'],
        'description': reddit_dict['title'],
        'extended': reddit_dict['description'],
        'tags': reddit_dict['tag'],
        'replace': 'no'
    }

    post_url = pinboard_base_url + add_post_snippet + pinboard_auth_snippet

    response = requests.get(post_url, params=args)
    # pdb.set_trace()
    print(response.text)
    return response


def import_reddit_url_from_file(filename):
    with open(filename, 'r') as infile:
        data = json.loads(infile.read())

    return data


if __name__ == "__main__":
    """
    You have to sleep for 3 seconds between requests or Maciej will Get Unhappy per
    https://pinboard.in/api
    """
    reddit_data = import_reddit_url_from_file("data.json")
    for entry in reddit_data:
        post_response = add_pin_url(entry)
        time.sleep(3)
    # print(post_response.text)
