import click

from arcli.worker.reader import Reader


@click.group(invoke_without_command=True)
@click.option('--arcli-file', envvar='ARCLI_FILE', default='arcli.yml')
@click.pass_context
def cli(ctx, arcli_file):
    ctx.obj = Reader(arcli_file)
    if ctx.invoked_subcommand is None:
        run()


@cli.command()
def run():
    """Default run command"""
    print()


if __name__ == "__main__":
    cli()
