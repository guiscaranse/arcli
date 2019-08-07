import logging
import traceback

import click

from arcli.exceptions.base import ArcliException
from arcli.worker.factory import Factory
from arcli.worker.reader import Reader


@click.group()
@click.option('--arcli-file', envvar='ARCLI_FILE', default='arcli.yml')
@click.option('--fancy/--no-fancy', default=False)
@click.pass_context
def cli(ctx, arcli_file, fancy):
    ctx.obj = (arcli_file, fancy)


@cli.command()
@click.pass_obj
def run(obj):
    """ Default run command """
    logging.basicConfig(filename='app.log', filemode='a', format='[%(levelname)s][%(asctime)s] %(message)s')
    try:
        logging.info("Starting Arcli")
        logging.info("Parse Arcli File")
        reader = Reader(obj[0])
        logging.info("Arcli file parsed")
        logging.info("Starting Arcli Factory")
        fact = Factory(reader)
        logging.info("Factory run")
        fact.run()
    except ArcliException as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        click.secho("[ERROR] Arcli failed to run: {}".format(click.style(e.message,
                                                                         fg='white',
                                                                         bg='red', bold=True)), fg="red")
    except Exception as e:
        logging.critical(e)
        logging.critical(traceback.format_exc())
        click.secho("[ERROR] Something failed in Arcli Interpreter: {}".format(click.style(e.__str__(),
                                                                                           fg='white',
                                                                                           bg='red',
                                                                                           bold=True)), fg="red")