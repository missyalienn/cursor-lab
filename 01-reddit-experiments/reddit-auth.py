
import os 
import praw


# get credentials from .env file
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')

# authenticate with Reddit
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)
#Test the connection
print("Auth successful. You can now use the Reddit API!")
print(reddit.read_only)

for submission in reddit.subreddit("test").hot(limit=10):
    print(submission.title)

# Output: 10 submissions