import argparse
import logging
import sys
import time
import requests

import json
import praw

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def munge_idiot_data(reddit_dict):
    """
    this function handles converting reddit relative urls to fully qualified urls.
    its extremely fucking unclear which *.url properties will give you fully qualified urls,
    so rather than handlign this properly by just fixing the broken ones, i'm going to inspect
    every url that comes through my apparatus.
    """
    protocol = 'https'
    # pdb.set_trace()
    for single_dict in reddit_dict:
        if protocol in single_dict['url']:
            pass
        else:
            single_dict['url'] = 'https://reddit.com' + single_dict['url']

    return reddit_dict



def get_all_posts(token, base_url):
    """
    returns a list of all pins in pinboard account
    """
    get_post_snippet = f"posts/all?auth_token={token}"
    pinboard_url = base_url + get_post_snippet

    return requests.get(pinboard_url)


def add_pin_url(reddit_dict, base_url, auth_snippet):
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

    post_url = base_url + add_post_snippet + auth_snippet
    response = requests.get(post_url, params=args)

    return response


def import_reddit_url_from_file(filename):
    """
    imports a list of reddit URLs and meta data from a file. 
    returns a json object of that data.
    """
    with open(filename, 'r') as infile:
        data = json.loads(infile.read())

    return data


def idb_excepthook(type, value, tb):
    """Call an interactive debugger in post-mortem mode
    If you do "sys.excepthook = idb_excepthook", then an interactive debugger
    will be spawned at an unhandled exception
    """
    if hasattr(sys, 'ps1') or not sys.stderr.isatty():
        sys.__excepthook__(type, value, tb)
    else:
        import pdb, traceback
        traceback.print_exception(type, value, tb)
        print
        pdb.pm()


def main(*args, **kwargs):
    parser = argparse.ArgumentParser(
        description="pynit: an integration between saved reddit posts and pinboard.")
    parser.add_argument(
        "--debug", "-d", action='store_true',
        help="Include debugging output")
    parser.add_argument(
        "--reddit-un", "-run", required=True, help="Reddit username")
    parser.add_argument(
        "--reddit-pw", "-rpw", required=True, help="Reddit password")
    parser.add_argument(
        "--reddit-cid", "-rcid", required=True, help="Reddit client id")
    parser.add_argument(
        "--reddit-sec", "-rsec", required=True, help="Reddit client secret")
    parser.add_argument(
        "--pb-apikey", "-pba", required=True, help="Pinboard api key")
    parsed = parser.parse_args()
    if parsed.debug:
        sys.excepthook = idb_excepthook
        LOGGER.setLevel(logging.DEBUG)

    reddit = praw.Reddit(client_id=parsed.reddit_cid,
                         client_secret=parsed.reddit_sec,
                         user_agent='/u/ pynit-tasks',
                         username=parsed.reddit_un,
                         password=parsed.reddit_pw
    )

    # this line is the most cursed line in programming
    # REDDIT.redditor,
    your_user = reddit.redditor(parsed.reddit_un)
    saved_posts = your_user.saved(limit=None)

    POSTS_TO_SAVE = []
    for link in saved_posts:
        if hasattr(link, 'is_self'):
            POSTS_TO_SAVE.append({
                'title': link.title,
                'tag': link.subreddit.display_name + ' added-by-pynnit',
                'description': link.selftext,
                'url': link.permalink
            })
        elif hasattr(link, 'is_root'):
            POSTS_TO_SAVE.append({
                'title': link.link_title,
                'tag': link.subreddit.display_name + ' added-by-pynnit',
                'description': link.body,
                'url': link.link_url
            })
        else:
            print("shit is fucked.")

    MUNGED_DATA = munge_idiot_data(POSTS_TO_SAVE)
    with open('data.json', 'w') as outfile:
        json.dump(MUNGED_DATA, outfile, indent=2)

    # handle the pinboard side of things
    pinboard_token = parsed.pb_apikey
    pinboard_base_url = "https://api.pinboard.in/v1/"
    pinboard_auth_snippet = f"?auth_token={pinboard_token}"

    """
    You have to sleep for 3 seconds between requests or Maciej will Get Unhappy
    per https://pinboard.in/api
    """
    reddit_data = import_reddit_url_from_file("data.json")
    for entry in reddit_data:
        post_response = add_pin_url(entry, pinboard_base_url, pinboard_auth_snippet)
        time.sleep(3)


if __name__ == '__main__':
    sys.exit(main(*sys.argv))
