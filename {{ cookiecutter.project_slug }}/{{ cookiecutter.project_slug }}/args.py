import logging
from argparse import ArgumentParser, Namespace
from pathlib import Path
from sys import argv
from typing import List

from {{cookiecutter.project_slug}}.__version__ import __version__
from {{cookiecutter.project_slug}}.utils import load_json_from_file


def argument_parser() -> ArgumentParser:
    """CLI argument parser"""
    args_parser = ArgumentParser("{{ cookiecutter.project_slug }}", description=("python3-app"))
    args_parser.add_argument("-V", "--version", action="version", version=__version__)
    args_parser.add_argument("-i", "--input", default=None, help="Input file")
    args_parser.add_argument("-o", "--output", default=None, help="Output directory")
    args_parser.add_argument("-H", "--extended_help", action="store_true", help="Show extended help and exit")
    args_parser.add_argument(
        "-d", "--debug", action="store_const", const=logging.DEBUG, default=logging.INFO, help="Show debug information",
    )
    return args_parser


def parse_args(arguments: List = argv[1:]) -> Namespace:
    """Parses a list into a namespace"""
    args, _ = argument_parser().parse_known_args(arguments)

    if args.extended_help:
        pass  # Implement method
        exit()

    if args.input:
        args.input = load_json_from_file(args.input)

    if args.output:
        args.output = Path(args.output)

    return args
