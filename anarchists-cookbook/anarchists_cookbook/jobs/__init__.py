from dagster import job, op
from assets.reddit_posts_comments_df import reddit_submissions
from resources import reddit_resource



@job(resource_defs={"reddit_client": reddit_resource.reddit_client})
def reddit_job():
    reddit_submissions()
