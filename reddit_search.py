import praw
import os

# your reddit credentials as env variables stored on your local machine.
reddit = praw.Reddit(client_id= os.environ.get('REDDIT_CLIENT_ID'),
                     client_secret= os.environ.get('REDDIT_CLIENT_SECRET'),
                     username= os.environ.get('REDDIT_USERNAME'),
                     password= os.environ.get('REDDIT_PASSWORD'),
                     user_agent= 'praw_ultron0.1')

def search_post(search_term, time_filter= 'all', post_count= 30):
    subreddit = reddit.subreddit('all')
    search_posts = subreddit.search(search_term, time_filter= time_filter, limit= post_count)
    results = {}
    for post in search_posts:
        if not post.stickied:
            results[post.title] = {'ups': post.ups, 'downs': post.downs, 'link': post.shortlink}

    return results

