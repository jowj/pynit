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
saved_posts = your_user.saved(limit=None)

posts_to_save = []
for link in saved_posts:
    try:
        posts_to_save.append([link.name, link.subreddit.display_name, link.url, link.author.name, link.title])
    except AttributeError:
        # only a comment, not a saved post
        pass

# printing for test
# print(posts_to_save)
    
with open('data.json', 'w') as outfile:
    json.dump(posts_to_save, outfile, indent=2)

