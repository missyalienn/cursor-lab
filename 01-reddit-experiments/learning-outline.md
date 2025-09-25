# Reddit API Learning Outline

**Goal**: Implement Reddit API concepts for production-ready ingestion


## Step 1: Get Credentials
**Action**: Create Reddit app and get API keys  
**Resource**: https://www.reddit.com/prefs/apps  
**File**: reddit-auth.py  
**Outcome**: Working client_id, client_secret, user_agent


## Step 2: Set Up Environment
**Action**: Configure secure credential storage  
**Resource**: Environment variables in ~/.zshrc  
**File**: reddit-auth.py  
**Outcome**: Credentials accessible via os.getenv()


## Step 3: Test Authentication  
**Action**: Verify Reddit API connection works  
**Resource**: https://praw.readthedocs.io/en/stable/getting_started/quick_start.html  
**File**: reddit-auth.py  
**Outcome**: Successful authentication confirmation


## Step 4: Understand Rate Limits
**Action**: Test API request timing and limits  
**Resource**: https://www.reddit.com/wiki/api (rate limit section)  
**File**: reddit-auth.py  
**Outcome**: Clear understanding of 60 req/min constraint


## Step 5: Extract Sample Data
**Action**: Fetch 10 posts from r/DIY and examine structure  
**Resource**: PRAW subreddit documentation  
**File**: fetch-data.py  
**Outcome**: JSON file with real Reddit post data


## Step 6: Implement Rate Limiting
**Action**: Add delays between requests, test with larger dataset  
**Resource**: time.sleep() and request timing  
**File**: fetch-with-limits.py  
**Outcome**: Stable fetching of 50+ posts without errors

## Step 7: Add Error Handling
**Action**: Handle network failures, API errors, malformed data  
**Resource**: Python exception handling patterns  
**File**: robust-fetch.py  
**Outcome**: Robust script that continues despite individual failures


## Step 8: Production Pipeline
**Action**: Remove noise, validate post quality, structure output  
**Resource**: Python regex and data validation  
**File**: production-pipeline.py  
**Outcome**: Clean, structured dataset ready for embedding


## Success Criteria
- [ ] Can authenticate reliably
- [ ] Understand rate limit constraints  
- [ ] Can fetch posts without breaking API rules
- [ ] Handle errors gracefully
- [ ] Produce clean, structured data
- [ ] Ready to build production system