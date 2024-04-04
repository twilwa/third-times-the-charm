from dagster import Definitions, load_assets_from_modules

# Assuming you have other assets defined in a module named `assets`
# and potentially other resources defined elsewhere
from .assets import reddit_posts_comments_df  # or however you've structured your assets
from .resources import reddit_resource  # Adjusted import

defs = Definitions(
    assets=load_assets_from_modules(reddit_posts_comments_df),  # Adjust as necessary
    resources={
        "reddit_client": reddit_resource.reddit_client()
        # Include other resources as before
    },
)
# TODO: import redditdatagenerator from .resources, see tutorial/__init__.py

