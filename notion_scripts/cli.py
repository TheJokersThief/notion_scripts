import click
import logging
from notion.client import NotionClient


from notion_scripts.config import Config
from notion_scripts.logging import setup_logger
from notion_scripts.booklist_info import BooklistInfo


@click.group(invoke_without_command=True)
@click.option('-c', '--config', help='Full path to TOML config file (If one doesn\'t exist at that path, it will be generated for you and no commands will be run)', type=click.Path())
@click.pass_context
def scripts(ctx, config):
    """
    A CLI wrapper for some helpful scripts I use on my personal Notion.
    """
    ctx.ensure_object(dict)
    ctx.obj['logger'] = setup_logger()
    ctx.obj['logger'].setLevel(logging.DEBUG)

    ctx.obj['config'] = Config.load_config(config)
    ctx.obj['logger'].debug("Parsed config: " + repr(ctx.obj['config']))

    ctx.obj['client'] = NotionClient(token_v2=ctx.obj['config'].get('token'))


@scripts.command()
@click.pass_context
@click.option('-p', '--page', help='Notion URL to page/database to be updated', type=str, default=None)
def booklist(ctx, page):
    """
    Updates the given page/database with information from the goodreads API by
    matching books based on title. You can configure the mapping of column names
    to API results in the config.
    """
    BooklistInfo(ctx, page)
