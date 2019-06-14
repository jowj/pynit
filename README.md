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
- [ ] Figure out how to differentiate between self.posts, link.posts, and comments
  - each one will have different fields but REDDIT DOESN'T DOCUMENT THIS
  - because reddit is stupid, that's why, i guess.

### Parse data 
Do i need to do anything here, actually, or is json fine?

### Putting data in pinboard
So far i've done nothing.
- [ ] Get regular auth to work
- [ ] Figure out how to post an item to my feed as public
- [ ] Figure out how to post an item to my feed as private
- [ ] Enable a conditional; NSFW items get posted as private, regular items as public.
- [ ] Iterate through a list.
