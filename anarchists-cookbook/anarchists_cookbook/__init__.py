from dagster import (
    Definitions,
    load_assets_from_modules,
)
from dotenv import load_dotenv

load_dotenv()
from dotenv import load_dotenv

from .assets import reddit_posts_comments_df
from .jobs import reddit_job
from .resources import reddit_client

load_dotenv()

assets = load_assets_from_modules([reddit_posts_comments_df])
jobs = [reddit_job]

# properly define the reddit client resource such that the environment vars are passed to the resource, allowing the asset to utilise the client resource when run.UserWarning: The environment variable REDDIT_CLIENT_ID is not set. Set it in your .env file to use the reddit_client resource.

defs = Definitions(
    resources={
        "reddit_client": reddit_client,
    },
    assets=assets,
    jobs=jobs,
)

# TODO: import redditdatagenerator from .resources, see tutorial/__init__.py

