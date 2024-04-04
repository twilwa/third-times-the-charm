from dagster import Definitions, load_assets_from_modules

# Assuming you have other assets defined in a module named `assets`
from .assets.reddit_posts_comments_df import reddit_submissions
from .resources.reddit_resource import reddit_client

defs = Definitions(
    assets=load_assets_from_modules([reddit_submissions]),  # Adjust as necessary
    resources={
        "reddit_client": reddit_client
        # Include other resources as before
    },
)
# TODO: import redditdatagenerator from .resources, see tutorial/__init__.py

