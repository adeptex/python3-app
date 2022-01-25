import logging
from argparse import Namespace
from typing import Dict

from {{cookiecutter.project_slug}}.args import parse_args
from {{cookiecutter.project_slug}}.constants import PROJECT_SLUG
from {{cookiecutter.project_slug}}.utils import printer


def main() -> None:
    """Main entry point"""
    args = parse_args()
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=args.debug)
    run(args)


def run(args: Namespace) -> Dict:
    outfile = args.output.joinpath("output.txt") if args.output else None
    printer(f"{PROJECT_SLUG}: {args}", outfile)


if __name__ == "__main__":
    main()
