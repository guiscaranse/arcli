import click


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        run()


@cli.command()
def run():
    """Default run command"""
    pass


if __name__ == "__main__":
    cli()
