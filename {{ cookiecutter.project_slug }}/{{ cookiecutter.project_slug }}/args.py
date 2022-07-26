import logging
from argparse import ArgumentParser, Namespace
from sys import argv
from typing import List

from {{cookiecutter.project_slug}}.__version__ import __version__


def argument_parser() -> ArgumentParser:  # pragma: no cover
    """CLI argument parser"""
    args_parser = ArgumentParser("{{ cookiecutter.project_slug }}", description=("{{ cookiecutter.project_slug }}"))
    args_parser.add_argument("-c", "--config", default=None, help="config filename")
    args_parser.add_argument("-o", "--output", default=None, help="output filename")
    args_parser.add_argument("-l", "--log", default=None, help="log filename")
    args_parser.add_argument(
        "--debug", action="store_const", const=logging.DEBUG, default=logging.INFO, help="show debug log",
    )
    args_parser.add_argument("--version", action="version", version=__version__, help="show version and exit")
    return args_parser


def parse_args(arguments: List = argv[1:]) -> Namespace:
    """Parses a list of arguments into a namespace"""
    args, _ = argument_parser().parse_known_args(arguments)

    if args.log:
        args.log = logging.FileHandler(args.log, mode="w")
    else:
        args.log = logging.StreamHandler()

    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=args.debug, handlers=[args.log])

    return args
