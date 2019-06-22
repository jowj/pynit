import praw
import json
import os
import pdb

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
    reddit = praw.Reddit(client_id=os.environ.get('REDDIT_ID'),
                         client_secret=os.environ.get('REDDIT_SECRET'),
                         user_agent='/u/ pynit-tasks',
                         username=os.environ.get('REDDIT_UN'),
                         password=os.environ.get('REDDIT_PW')
    )

    your_user = reddit.redditor(os.environ.get('REDDIT_UN'))
    saved_posts = your_user.saved(limit=None)

    posts_to_save = []
    for link in saved_posts:
        if hasattr(link, 'is_self'):
            posts_to_save.append({'title':link.title, 'tag':link.subreddit.display_name + ' added-by-pynnit', 'description':link.selftext, 'url':link.permalink})
        elif hasattr(link, 'is_root'):
            posts_to_save.append({'title':link.link_title, 'tag':link.subreddit.display_name + ' added-by-pynnit', 'description':link.body, 'url':link.link_url})
        else:
            print("shit is fucked.")

    munged_data = munge_idiot_data(posts_to_save)
    with open('data.json', 'w') as outfile:
        json.dump(munged_data, outfile, indent=2)

