import logging
from argparse import Namespace
from typing import Dict, Iterable

from {{cookiecutter.project_slug}}.__version__ import __version__
from {{cookiecutter.project_slug}}.args import parse_args
from {{cookiecutter.project_slug}}.utils import load_yaml_file


def main() -> None:  # pragma: no cover
    """Main entry point"""
    args = parse_args()
    logging.info(f"{{cookiecutter.project_name}} v{__version__}")

    config = load_yaml_file(args.config)

    [*map(print, run(args, config))]

    logging.info(f"{{cookiecutter.project_name}} v{__version__} done")


def run(args: Namespace, config: Dict = {}) -> Iterable:
    """Main worker process"""
    yield from range(10)


if __name__ == "__main__":
    main()
