__version__ = '0.0.1'
import logging
import click
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(message)s')
LOGGER = logging.getLogger(__name__)
@click.command()
@click.argument('left_file',type=click.Path(exists=True))
@click.argument('right_file',type=click.Path(exists=True))
@click.option( '--on', help="Common column to use for both files.  Column must exist in both files")
@click.option( '--left_on', help="Column to join on from left file. If supplied, then right_on must also be supplied.")
@click.option( '--right_on', help="Column to join on from right file.  If supplied, then left_on must also be supplied.")
@click.option( '--join', default='outer', help='join type: inner, outer.   Defaults to outer.',
              type=click.Choice(['outer', 'inner', 'left', 'right']))

@click.option('-o', '--output',help='(optional) name of file to write data into. ')
@click.option('-d', '--dryrun', is_flag=True, help='If set, will only gather data and not write')
@click.option('-v', '--verbose', is_flag=True, help='Enables verbose logging mode')
@click.option('-q', '--quiet', is_flag=True,help='Limits logging output to warnings and errors. ')
@click.version_option(version=__version__)
@click.help_option()
@click.pass_context
def cli(ctx, **kwargs):
    """
    Join 2 csv files on a specific column. Wrapper around pandas dataframe merge().
    See [pandas dataframe.merge doc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) for join behavior.

    defaults to outer join

    Usage:

   Left Join two files on a column named 'id'
    poetry run python ./src/csvmerge.py ./data/left.csv ./data/right.csv  --join left --on id  --output left_output.csv --verbose

   Outer Join two files.   Left file join on column named 'id', right file on 'alt_id'
   poetry run python ./src/csvmerge.py ./data/left.csv ./data/right.csv  --join outer --left_on id  --right_on alt_id --output outer_output.csv --verbose


    """
    ctx.ensure_object(dict)
    args = ctx.obj #obj is dict that is shared among all command invocations
    args.update(**kwargs)

    if kwargs.get('quiet'):
        LOGGER.setLevel(logging.WARNING)
    if kwargs.get('verbose'):
        LOGGER.setLevel(logging.DEBUG)

    df_left  = pd.read_csv(kwargs.get('left_file'))
    df_right = pd.read_csv(kwargs.get('right_file'))

    how = kwargs.get('join')

    LOGGER.debug("File[%s] has %d rows excluding header", kwargs.get('left'), len(df_left))
    LOGGER.debug("File[%s] has %d rows excluding header", kwargs.get('right'), len(df_right))

    left_on = kwargs.get('on')
    if left_on:
        right_on = left_on
    else:
        left_on  = kwargs.get('left_on')
        right_on = kwargs.get('right_on')
    if not left_on or not right_on:
        print("ERROR:  must supply either an --on param, or both --left_on and --right_on")
        exit(-1)

    #defaults to inner
    df = pd.merge(df_left, df_right, left_on=left_on, right_on=right_on,
                  how=how, suffixes=('_left', '_right'))
    df.fillna('',inplace=True)
    LOGGER.debug("After merge. df has %d rows excluding header", len(df))

    if kwargs.get('dryrun'):
        LOGGER.info("Dryrun.  skipping output")
    else:
        output = kwargs.get('output')
        df.to_csv(output,  encoding='utf-8', index=False)
        LOGGER.info("Output to file[%s]", output)

if __name__ == '__main__':
    cli(obj={})
