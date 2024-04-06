from logging import info
from sys import argv
from typing import List

from {{cookiecutter.project_slug}}.__version__ import __version__
from {{cookiecutter.project_slug}}.args import parse_args


def main(arguments: List = argv[1:]) -> None:
    """Main entry point"""
    args = parse_args(arguments)

    info(f"{{cookiecutter.project_name}} v{__version__}")

    [*map(print, args)]

    info(f"{{cookiecutter.project_name}} v{__version__} done")


if __name__ == "__main__":
    main()
