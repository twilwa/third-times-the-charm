from dagster import asset, envVar
from praw import Reddit
#TODO: import RedditDataGenerator, define "redditclient": datagen, see connecting to external services
@asset
def reddit_posts():
    """
    This asset returns a dataframe of Reddit posts. The list contains 10 instances of the .hot, .top, 
    and .controversial posts on the subreddit of the day, for a total of 30 items.
    """
    return list(Reddit)
