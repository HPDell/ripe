from typing import Dict, Tuple
import sys
import subprocess
import click
from prettytable import PrettyTable, from_json

@click.command('list')
@click.option('--library', type=click.Path(file_okay=False), default='', help='Path to library')
@click.option('--columns', '-c', multiple=True, help='Additional columns to show.')
def list_packages(library, columns):
    args: Dict[str, str] = dict()
    if (library != ''):
        args['library'] = library
    sel_cols = ['package', 'version', 'repository'] + list(columns)
    cmd = 'cat(jsonify::to_json(pak::pkg_list({})[c({})]))'.format(
        ', '.join([f'{k} = {v}' for k, v in args.items()]),
        ', '.join([f'"{x}"' for x in sel_cols])
    )
    r_proc = subprocess.run(['Rscript', '-e', cmd], capture_output=True)
    if r_proc.returncode != 0:
        print(r_proc.stderr.decode())
        exit(1)
    out = from_json(r_proc.stdout.decode())
    out.align = 'l'
    print(out)
