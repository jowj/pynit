import praw
import json
import os
import pdb

# Handle reddit requests
reddit = praw.Reddit(client_id=os.environ.get('REDDIT_ID'),
                     client_secret=os.environ.get('REDDIT_SECRET'),
                     user_agent='/u/ pynit-tasks',
                     username = os.environ.get('REDDIT_UN'),
                     password = os.environ.get('REDDIT_PW')
                     )

your_user = reddit.redditor(os.environ.get('REDDIT_UN'))
saved_posts = your_user.saved(limit=1)

posts_to_save = []
for link in saved_posts:
    if hasattr(link, 'is_self'):
        posts_to_save.append({'title':link.title, 'tag':link.subreddit.display_name, 'author':link.author.name, 'description':link.selftext, 'url':link.permalink})
    elif hasattr(link, 'is_root'):
        posts_to_save.append({'title':link.link_title, 'tag':link.subreddit.display_name, 'author':link.author.name, 'description':link.body, 'url':link.link_url})
    else:
        print("shit is fucked.")


# print(posts_to_save)
with open('data.json', 'w') as outfile:
    json.dump(posts_to_save, outfile, indent=2)

