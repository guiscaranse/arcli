import click

from arcli.worker.factory import Factory
from arcli.worker.reader import Reader


@click.group()
@click.option('--arcli-file', envvar='ARCLI_FILE', default='arcli.yml')
@click.option('--fancy', default=True)
@click.pass_context
def cli(ctx, arcli_file, fancy):
    ctx.obj = Reader(arcli_file)


@cli.command()
@click.pass_obj
def run(reader):
    """ Default run command """
    fact = Factory(reader)
    fact.run()
    pass
