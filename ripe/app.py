import click
from pkg_install import install_packages

@click.group()
def main():
    pass

main.add_command(install_packages)

if __name__ == '__main__':
    main()
