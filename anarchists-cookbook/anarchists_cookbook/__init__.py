from dagster import Definitions, load_assets_from_modules
from .resources.reddit_resource import reddit_client_resource  # Adjusted import

# Assuming you have other assets defined in a module named `assets`
# and potentially other resources defined elsewhere
from .assets import reddit_posts_comments_df  # or however you've structured your assets

defs = Definitions(
    assets=load_assets_from_modules('reddit_posts_comments_df.assets'),  # Adjust as necessary
    resources={
        "reddit_client": reddit_client_resource,  # Adjusted to reference the resource correctly
        # Include other resources as before
    },
)
#TODO: import redditdatagenerator from .resources, see tutorial/__init__.py