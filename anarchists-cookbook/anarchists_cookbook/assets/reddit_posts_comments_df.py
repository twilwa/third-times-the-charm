import os
import pandas as pd
from dagster import asset, OpExecutionContext, Field, StringSource, IntSource, List
from dagster_pandas import PandasColumn, create_dagster_pandas_dataframe_type

RedditSubmissionsDataFrame = create_dagster_pandas_dataframe_type(
    name="RedditSubmissionsDataFrame",
    columns=[
        PandasColumn.string_column("subreddit", non_nullable=True),
        PandasColumn.string_column("category", non_nullable=True),
        PandasColumn.string_column("title", non_nullable=True),
        PandasColumn.string_column("url", non_nullable=True),
        PandasColumn.string_column("text_content"),
        PandasColumn.string_column("comments"),
    ],
)


@asset(
    required_resource_keys={"reddit_client"},
    config_schema={
        "subreddit_names": Field(
            List[str],
            default_value=["all"],
            description="The names of the subreddits to fetch submissions from.",
        ),
        "submissions_limit": Field(
            int,
            default_value=5,
            description="The number of submissions to fetch from each category.",
        ),
        "comments_limit": Field(
            int,
            default_value=20,
            description="The number of comments to fetch from each submission.",
        ),
    },
    output_asset_type=RedditSubmissionsDataFrame,
)
def reddit_submissions(context: OpExecutionContext):
    reddit = context.resources.reddit_client
    subreddit_names = context.op_config["subreddit_names"]
    submissions_limit = context.op_config["submissions_limit"]
    comments_limit = context.op_config["comments_limit"]

    submissions_data = {
        "subreddit": [],
        "category": [],
        "title": [],
        "url": [],
        "text_content": [],
        "comments": [],
    }

    for subreddit_name in subreddit_names:
        subreddit = reddit.subreddit(subreddit_name)

        categories = ["top", "controversial", "hot"]
        for category in categories:
            for submission in getattr(subreddit, category)(limit=submissions_limit):
                submissions_data["subreddit"].append(subreddit_name)
                submissions_data["category"].append(category)
                submissions_data["title"].append(submission.title)
                submissions_data["url"].append(submission.url)
                submissions_data["text_content"].append(submission.selftext)

    df = pd.DataFrame(submissions_data)
    output_path = os.path.join(
        context.run_config["output_dir"], "reddit_submissions.csv"
    )
    df.to_csv(output_path, index=False)

    return df
