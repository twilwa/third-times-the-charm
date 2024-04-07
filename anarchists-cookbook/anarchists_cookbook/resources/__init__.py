from dagster import Definitions, load_assets_from_modules, define_asset_job, AssetSelection
from ..assets import reddit_posts_comments_df  # Ensure this import is correct
from .reddit_resource import reddit_client

# Load assets
reddit_assets = load_assets_from_modules([reddit_posts_comments_df])

# Define resources and jobs
defs = Definitions(
    assets=reddit_assets,  # Directly use the loaded assets
    resources={"reddit_client": reddit_client},
)

# Define a job for specific assets if needed
reddit_submissions_job = define_asset_job(
    "reddit_submissions_job",
    selection=AssetSelection.all()),

