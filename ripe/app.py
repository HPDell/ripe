import click
from pkg_install import install_packages
from pkg_list import list_packages

@click.group()
def main():
    pass

main.add_command(install_packages)
main.add_command(list_packages)

if __name__ == '__main__':
    main()
