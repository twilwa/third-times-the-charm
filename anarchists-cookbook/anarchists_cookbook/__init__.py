from dagster import Definitions, load_assets_from_modules, EnvVar, define_asset_job, AssetSelection
from .assets import reddit_posts_comments_df  # Ensure this import is correct
from .resources import reddit_client
from dotenv import load_dotenv
load_dotenv()

defs = Definitions(
    resources={
        "reddit_client": reddit_client.configured({
            "client_id": {"env": "REDDIT_CLIENT_ID"},
            "client_secret": {"env": "REDDIT_CLIENT_SECRET"},
            "username": {"env": "REDDIT_USERNAME"},
            "password": {"env": "REDDIT_PASSWORD"},
            # "user_agent" is optional and has a default value
        })
    },
    assets=load_assets_from_modules([reddit_posts_comments_df]),
)


# TODO: import redditdatagenerator from .resources, see tutorial/__init__.py
