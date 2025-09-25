
import os 
import praw
from dotenv import load_dotenv

# Load .env from project root
load_dotenv('.env')

# get credentials from environment variables
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT') or "TestScript/1.0 by /u/yourusername"

print(f"Client ID: {client_id}")
print(f"Client Secret: {client_secret}")
print(f"User Agent: {user_agent}")

# authenticate with Reddit
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
)
#Test the connection
print("Auth successful. You can now use the Reddit API!")
print(reddit.read_only)

#Test the connection by printing title of first 10 submissions r/test
# for submission in reddit.subreddit("test").hot(limit=10):
    # print(submission.title)

subreddit = reddit.subreddit("diy")
print(subreddit.display_name)
print(subreddit.title)
print(subreddit.description)
print(subreddit.public_description)
print(subreddit.subscribers)

