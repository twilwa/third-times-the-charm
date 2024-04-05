from dagster import (
    Definitions,
    load_assets_from_modules,
    AssetSelection,
    define_asset_job,
    ScheduleDefinition,
    EnvVar,
)

from . import assets

# Assuming you have other assets defined in a module named `assets`

from .resources.reddit_resource import reddit_client

from .assets.reddit_posts_comments_df import reddit_submissions

defs = Definitions(
    assets=load_assets_from_modules([assets]),  # Adjust as necessary
    resources={
        "reddit_client": reddit_client
        # Include other resources as before
    },
)
# TODO: import redditdatagenerator from .resources, see tutorial/__init__.py
