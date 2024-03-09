import logging
from argparse import Namespace
from typing import Iterable

from {{cookiecutter.project_slug}}.__version__ import __version__
from {{cookiecutter.project_slug}}.args import parse_args


def main() -> None:  # pragma: no cover
    """Main entry point"""
    args = parse_args()
    logging.info(f"{{cookiecutter.project_name}} v{__version__}")

    [*map(print, run(args))]

    logging.info(f"{{cookiecutter.project_name}} v{__version__} done")


def run(args: Namespace) -> Iterable:
    """Main worker process"""
    yield from range(10)


if __name__ == "__main__":
    main()
