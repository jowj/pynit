import json
import os
import praw


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


if __name__ == "__main__":
    REDDIT = praw.Reddit(client_id=os.environ.get('REDDIT_ID'),
                         client_secret=os.environ.get('REDDIT_SECRET'),
                         user_agent='/u/ pynit-tasks',
                         username=os.environ.get('REDDIT_UN'),
                         password=os.environ.get('REDDIT_PW')
    )

    # this line is the most cursed line in programming
    # REDDIT.redditor,
    YOUR_USER = REDDIT.redditor(os.environ.get('REDDIT_UN'))
    SAVED_POSTS = YOUR_USER.saved(limit=None)

    POSTS_TO_SAVE = []
    for link in SAVED_POSTS:
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
