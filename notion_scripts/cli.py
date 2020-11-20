import click
from notion_scripts.config import Config


@click.group()
@click.option('-c', '--config', help='Full path to TOML config file')
@click.pass_context
def scripts(ctx, config):
    """A CLI wrapper for the API of Public scripts."""
    ctx.ensure_object(dict)
    ctx.obj['config'] = Config.load_config(config)
    click.echo("Parsed config: " + repr(ctx.obj['config']))


@scripts.command()
def test():
    pass
