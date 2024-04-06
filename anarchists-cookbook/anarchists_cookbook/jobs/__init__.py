from dagster import job
from ..assets.reddit_posts_comments_df import reddit_submissions
from ..resources import reddit_client_resource


@job(resource_defs={"reddit_client": reddit_client_resource})
def reddit_job():
    reddit_submissions()
