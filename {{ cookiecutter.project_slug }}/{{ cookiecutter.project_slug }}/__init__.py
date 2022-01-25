from typing import Dict


def run(arguments: str) -> Dict:
    """
    Boilerplate for simplifying usage and integration.

    import {{ cookiecutter.project_slug }}
    for item in {{ cookiecutter.project_slug }}.run("-i file.json"):
        print(item)
    """
    import shlex

    from {{cookiecutter.project_slug}}.args import parse_args
    from {{cookiecutter.project_slug}}.main import run

    argv = shlex.split(arguments)
    args = parse_args(argv)
    return run(args)
