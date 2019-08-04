import click

from arcli.worker.reader import Reader


@click.group()
@click.option('--arcli-file', envvar='ARCLI_FILE', default='arcli.yml')
@click.pass_context
def cli(ctx, arcli_file):
    ctx.obj = Reader(arcli_file)


@cli.command()
@click.pass_obj
def run(reader):
    reader.teste()
    """ Default run command """
    pass
