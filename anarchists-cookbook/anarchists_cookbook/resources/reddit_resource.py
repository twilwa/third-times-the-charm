from dataclasses import dataclass
from dagster import ConfigurableResource, Field, StringSource
import praw

@dataclass
class RedditClientConfig:
    client_id: str
    client_secret: str
    user_agent: str
    username: str
    password: str

class RedditClientResource(ConfigurableResource):
    def __init__(self, config: RedditClientConfig):
        self.reddit = praw.Reddit(
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent=config.user_agent,
            username=config.username,
            password=config.password,
        )

    @staticmethod
    def config_schema():
        return {
            "client_id": Field(StringSource),
            "client_secret": Field(StringSource),
            "user_agent": Field(StringSource),
            "username": Field(StringSource),
            "password": Field(StringSource),
        }

    def get_client(self):
        return self.reddit

# Optional: For complex data transformations
class RedditDataTranslator:
    @staticmethod
    def translate(submission):
        # Example translation method
        return {
            "title": submission.title,
            "url": submission.url,
            "content": submission.selftext,
        }