from dagster import resource, Field, StringSource
import praw


@resource(
    {
        "client_id": Field(StringSource),
        "client_secret": Field(StringSource),
        "user_agent": Field(
            StringSource, is_required=False, default_value="dagster_reddit_client/0.1"
        ),
        "username": Field(StringSource),
        "password": Field(StringSource),
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

