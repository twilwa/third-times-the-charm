from dagster import resource, Field, StringSource
from dagster import EnvVar
import praw
from dotenv import load_dotenv

load_dotenv()


@resource(
    {
        "client_id": Field(EnvVar, is_required=True),
        "client_secret": Field(EnvVar, is_required=True),
        "user_agent": Field(
            EnvVar, is_required=False, default_value="dagster_reddit_client/0.1"
        ),
        "username": Field(EnvVar, is_required=True),
        "password": Field(EnvVar, is_required=True),
    }
)
def reddit_client(init_context):
    return praw.Reddit(
        client_id=init_context.resource_config["client_id"],
        client_secret=init_context.resource_config["client_secret"],
        user_agent=init_context.resource_config.get("user_agent"),
        username=init_context.resource_config["username"],
        password=init_context.resource_config["password"],
    )
