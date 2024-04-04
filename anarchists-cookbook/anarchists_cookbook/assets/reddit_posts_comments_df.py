from dagster import asset, OpExecutionContext, Field, StringSource
from pandasai import SmartDataframe
import pandasai as pd

@asset(
    required_resource_keys={"reddit_client"},
    config_schema={
        "subreddit_name": Field(StringSource, default_value="python", description="The name of the subreddit to fetch submissions from."),
        "submissions_limit": Field(int, default_value=5, description="The number of submissions to fetch from each category.")
    }
)
def reddit_submissions(context: OpExecutionContext):
    reddit = context.resources.reddit_client
    subreddit_name = context.op_config["subreddit_name"]
    submissions_limit = context.op_config["submissions_limit"]
    subreddit = reddit.subreddit(subreddit_name)

    categories = ["top", "controversial", "hot"]
    submissions_data = {
        "category": [],
        "title": [],
        "url": [],
        "text_content": [],
    }

    for category in categories:
        for submission in getattr(subreddit, category)(limit=submissions_limit):
            submissions_data["category"].append(category)
            submissions_data["title"].append(submission.title)
            submissions_data["url"].append(submission.url)
            submissions_data["text_content"].append(submission.selftext)

    return pd.SmartDataframe(submissions_data)
