
import os 
import praw
import time 
import json 
from dotenv import load_dotenv

# Load .env from project root
load_dotenv('.env')

# get credentials from environment variables
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT') or "TestScript/1.0 by /u/yourusername"

#print(f"Client ID: {client_id}")
print(f"User Agent: {user_agent}")

# authenticate with Reddit
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
)
#Test the connection
print("Reddit API authentication successful.")

#Test the connection by printing title of first 10 submissions r/test
# for submission in reddit.subreddit("test").hot(limit=10):
    # print(submission.title)

#Create connection to r/diy
subreddit = reddit.subreddit("diy")

# Create an empty list to store all post data
all_data = []  
post_counter = 1

#For top 10 posts from r/diy last month, create a dictionary to store post data 
for submission in reddit.subreddit("diy").top(time_filter="month", limit=10):
    
    # Create a dictionary to store post data
    post_data = {
        'post_id': submission.id,
        'title': submission.title,
        'content': submission.selftext,
        'score': submission.score,
        'permalink': f"https://reddit.com{submission.permalink}",
        'comments': []  # Store comments in a list for this post
    }
    
    # Get comments FOR THIS SPECIFIC POST
    submission.comments.replace_more(limit=0)
    for i, comment in enumerate(submission.comments):
        if i >= 5:  # Stop after 5 comments
            break
        # Store comment data WITH reference to this post
        comment_data = {
            'post_id': submission.id,  # Link back to parent post
            'comment_id': comment.id,
            'body': comment.body,
            'score': comment.score
        }
        post_data['comments'].append(comment_data)
    
    all_data.append(post_data)
    time.sleep(1.2)
  
    print(f"Processed post:{post_counter} - {submission.title[:50]}...")
    print(f"Stored top {len(post_data['comments'])} comments")
    post_counter += 1

    # Save to JSON file
    #with open('reddit-test-data.json', 'w') as f:
        #json.dump(all_data, f, indent=4)