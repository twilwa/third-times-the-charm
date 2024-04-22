from dagster import resource, Field, StringSource
from dagster import EnvVar
import praw
from dotenv import load_dotenv

load_dotenv()


@resource(
    {
        "REDDIT_CLIENT_ID": Field(StringSource, is_required=True),
        "REDDIT_CLIENT_SECRET": Field(StringSource, is_required=True),
        "user_agent": Field(
            StringSource, is_required=False, default_value="dagster_reddit_client/0.1"
        ),
        "REDDIT_USERNAME": Field(StringSource, is_required=True),
        "REDDIT_PASSWORD": Field(StringSource, is_required=True),
    }
)
def reddit_client(init_context):
    return praw.Reddit(
        client_id=init_context.resource_config["REDDIT_CLIENT_ID"],
        client_secret=init_context.resource_config["REDDIT_CLIENT_SECRET"],
        user_agent=init_context.resource_config.get("user_agent"),
        username=init_context.resource_config["REDDIT_USERNAME"],
        password=init_context.resource_config["REDDIT_PASSWORD"],
    )
