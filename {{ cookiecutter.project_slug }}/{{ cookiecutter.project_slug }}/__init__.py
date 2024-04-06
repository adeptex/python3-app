from typing import Dict


def run(arguments: str) -> Dict:
    """
    Boilerplate for simplifying usage and integration.

    import {{ cookiecutter.project_slug }}
    for item in {{ cookiecutter.project_slug }}.run("-l log.txt --debug ..."):
        print(item)
    """
    import shlex

    from {{cookiecutter.project_slug}}.main import main

    argv = shlex.split(arguments)
    return main(argv)
