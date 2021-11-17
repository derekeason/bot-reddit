import praw
from decouple import config


reddit = praw.Reddit(
    client_id=config('CLIENT_ID'),
    client_secret=config('CLIENT_SECRET'),
    user_agent=config('USER_AGENT'),
)

for submission in reddit.subreddit('wallstreetbets').hot(limit=10):
    for comment in submission.comments:
        if hasattr(comment, 'body'):
            if ' moon ' in comment.body:
                print('----------')
                print(comment.body)
