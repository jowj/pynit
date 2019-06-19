# pynit
an integration between saved reddit posts and pinboard

## Outline:
### Getting data from reddit
Currently i'm getting only the first page of saved, no NSFW items
- [X] refactor to use praw instead of requests
  - praw has more functionality more obviously than I can figure out with requests.
  - its aggrevating.
- [X] Figure out how to pull the entire list
  - in praw this is done through "limit=None" arg.
- [X] Figure out how to enable pulling NSFW items
  - in praw this is actually just done by default
- [X] Figure out how to differentiate between self.posts, link.posts, and comments
  - each one will have different fields but REDDIT DOESN'T DOCUMENT THIS
  - because reddit is stupid, that's why, i guess.

### Parse data 
Do i need to do anything here, actually, or is json fine?

### Putting data in pinboard
So far i've done nothing.
- [X] Get auth token to work
  - Finally got this to work; I had a fundamental mistunderstanding of what pinboard meant by "method" in the URL.
- [X] Figure out how to pull existing posts
- [ ] Figure out how to post an item to my feed as public
- [ ] Figure out how to post an item to my feed as private
- [ ] Enable a conditional; NSFW items get posted as private, regular items as public.
- [ ] Iterate through a list.

### IF WE RECEIVE OVER 5 MILLION DOLLARS I WILL:
- [ ] figure out how the fuck to compare urls/titles against already existing entries in pinboard
  - and obviously don't add dupes
- [ ] figure out how to pull in RES saved items; that'll be weird slash impossible maybe


## Information about reddit (i'm so sorry)
So, there are multiple kinds of reddit posts, and each kind of reddit post seems to have distinct names for the same things, which is REALLY fucking annoying. Its extra frustrating because there's not just a quick lookup for this, you have to just dig through Too Much json.

If you're using PRAW, a reddit /post/ has an attribute called `.is_self` that's boolean. If its true, its a text only post, if its false then its a link post.

Reddit comments do not have this attribute. They DO have an attribute called `.is_root`, which i use to differentiate themm.
