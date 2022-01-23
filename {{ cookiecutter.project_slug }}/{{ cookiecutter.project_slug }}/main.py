import logging

from {{cookiecutter.project_slug}}.args import parse_args
from {{cookiecutter.project_slug}}.constants import PROJECT_SLUG
from {{cookiecutter.project_slug}}.utils import printer


def main() -> None:
    """Main entry point"""
    args = parse_args()
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=args.debug)

    outfile = args.output.joinpath("output.txt") if args.output else None

    printer(PROJECT_SLUG, outfile)


if __name__ == "__main__":
    main()
