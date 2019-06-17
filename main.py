import pdb
import praw
import json
import os

reddit = praw.Reddit(client_id=os.environ.get('REDDIT_ID'),
                     client_secret=os.environ.get('REDDIT_SECRET'),
                     user_agent='/u/ pynit-tasks',
                     username = os.environ.get('REDDIT_UN'),
                     password = os.environ.get('REDDIT_PW')
                     )

your_user = reddit.redditor(os.environ.get('REDDIT_UN'))
saved_posts = your_user.saved(limit=50)

posts_to_save = []
for link in saved_posts:
    if hasattr(link, 'is_self'):
        posts_to_save.append([link.title, link.subreddit.display_name, link.author.name, link.selftext, link.url, link.permalink])
    elif hasattr(link, 'is_root'):
        # pdb.set_trace()
        posts_to_save.append([link.link_title, link.subreddit.display_name, link.author.name, link.body, link.link_url])
    else:
        pdb.set_trace()

with open('data.json', 'w') as outfile:
    json.dump(posts_to_save, outfile, indent=2)
