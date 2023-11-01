from typing import Dict, Tuple
import os
import click

@click.command('install')
@click.option('--library', type=click.Path(file_okay=False), default='', help='Package library to install the packages to.')
@click.option('--upgrade', type=int, default=False, help='When FALSE, the default, pak does the minimum amount of work to give you the latest version(s) of pkg. When upgrade = TRUE, pak will ensure that you have the latest version(s) of pkg and all their dependencies.')
@click.option('--dependencies', type=int, default=-1, help='What kinds of dependencies to install. Most commonly one of the following values: NA (only required), TRUE (all), and FALSE (no dependencies).')
@click.argument('pkgs', nargs=-1)
def install_packages(library: str, upgrade: bool, dependencies: int, pkgs: Tuple[str]):
    args: Dict[str, str] = {
        'pkg': 'c({})'.format(', '.join([f'"{x}"' for x in pkgs]))
    }
    if library.strip() != '':
        args['lib'] = library
    if upgrade == True:
        args['upgrade'] = 'TRUE'
    if dependencies >= 0:
        args['dependencies'] = {
            -1: "NA",
            0: "FALSE",
            1: "TRUE"
        }[dependencies]
    cmd = 'Rscript --vanilla -e \'pak::pkg_install({})\''.format(', '.join([f'{k} = {v}' for k, v in args.items()]))
    os.system(cmd)
    
