from argparse import ArgumentParser, Namespace
from logging import DEBUG, INFO, FileHandler, StreamHandler, basicConfig
from typing import List

from {{cookiecutter.project_slug}}.__version__ import __version__


def argument_parser() -> ArgumentParser:  # pragma: no cover
    """CLI argument parser"""
    args_parser = ArgumentParser("{{ cookiecutter.project_slug }}", description=("{{ cookiecutter.project_slug }}"))
    args_parser.add_argument("-l", "--log", default=None, help="Log file")
    args_parser.add_argument(
        "--debug",
        action="store_const",
        const=DEBUG,
        default=INFO,
        help="Show debug log",
    )
    args_parser.add_argument("--version", action="version", version=__version__, help="Show version and exit")
    return args_parser


def parse_args(arguments: List) -> Namespace:
    """Parses a list of arguments into a namespace"""
    args, _ = argument_parser().parse_known_args(arguments)

    if args.log:
        args.log = FileHandler(args.log, mode="w")
    else:
        args.log = StreamHandler()

    basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=args.debug, handlers=[args.log])

    return args
