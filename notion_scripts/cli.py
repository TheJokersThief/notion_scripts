import click
import logging
from notion.client import NotionClient


from notion_scripts.config import Config
from notion_scripts.logging import setup_logger
from notion_scripts.booklist_info import BooklistInfo


@click.group()
@click.option('-c', '--config', help='Full path to TOML config file', type=click.Path())
@click.pass_context
def scripts(ctx, config):
    """A CLI wrapper for the API of Public scripts."""
    ctx.ensure_object(dict)
    ctx.obj['logger'] = setup_logger()
    ctx.obj['logger'].setLevel(logging.DEBUG)

    ctx.obj['config'] = Config.load_config(config)
    ctx.obj['logger'].info("Parsed config: " + repr(ctx.obj['config']))

    ctx.obj['client'] = NotionClient(token_v2=ctx.obj['config'].get('token'))


@scripts.command()
def test():
    pass


@scripts.command()
@click.pass_context
def booklist(ctx):
    BooklistInfo(ctx)
