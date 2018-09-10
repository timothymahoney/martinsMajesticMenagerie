#!/usr/bin/env python
#
"""
@author: Adam Kniffen <adamkniffen@gmail.com>
@updated: 04Sep2018
"""

import click
from app.core.menagerie import app
import sys


@click.command()
@click.argument('apitarget', nargs=1)
@click.option('--processonly', is_flag=True, help="Work with existing raw data")
@click.option('--normalize', default=False, is_flag=True, help="Normalize the data into a single table")
def main(**kwargs):
    # get our class instance
    op = app()
    if kwargs['apitarget'] not in op.collectTargetTypes().keys():
        sys.exit("invalid api target specified!")

    # other checks

    # collect

    if kwargs['processonly'] is False:
        op.collectTarget()

    if kwargs['processonly'] is not False:
        op.normalize()


if __name__ == "__main__":
    main()