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
saved_posts = your_user.saved(limit=20)

posts_to_save = []
for link in saved_posts:
    if hasattr(link, 'is_self'):
        posts_to_save.append([link.name, link.subreddit.display_name, link.author.name, link.selftext, link.title])
    elif hasattr(link, 'is_root'):    
        posts_to_save.append([link.name, link.subreddit.display_name, link.body, link.author.name])
        # pdb.set_trace()
    else:
        pdb.set_trace()
            
with open('data.json', 'w') as outfile:
    json.dump(posts_to_save, outfile, indent=2)

