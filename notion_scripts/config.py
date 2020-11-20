import click
import toml
import sys

from marshmallow import Schema, fields, INCLUDE, ValidationError
from pprint import pprint
from os import path


class Config(Schema):
    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

    class BooklistInfoSchema(Schema):
        page = fields.Str(default="https://www.notion.so/<some_org_id>/<a_page_id>")
        goodreads_api_token = fields.Str(default="Get a token from https://www.goodreads.com/api/keys")
        columns = fields.Dict(
            keys=fields.Str(), values=fields.Str(),
            default={
                "pages": "num_pages",
                "publication_year": "publication_year",
                "publication_month": "publication_month",
                "publication_day": "publication_day",
                "rating": "average_rating",
                "name": "title",
            }
        )

    token = fields.Str(default="<token_v2>")
    booklist_info = fields.Nested(BooklistInfoSchema, default=BooklistInfoSchema())

    @staticmethod
    def load_config(config_location):
        # If config doesn't exist, write the defaults to it
        if not path.exists(config_location):
            with open(config_location, mode="w") as conf:
                click.echo(f"Config at {config_location} doesn't exist, writing a blank config and exiting")
                toml.dump(Config().dump(object()), conf)
                sys.exit(1)

        with open(config_location, mode="r") as conf:
            data = toml.load(conf)
        try:
            global CONFIG
            CONFIG = Config().load(data)
            return CONFIG
        except ValidationError as error:
            print("ERROR: package.json is invalid")
            pprint(error.messages)
            sys.exit(1)
