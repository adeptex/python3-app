from setuptools import find_packages, setup
from importlib import import_module

install_requires = ["yaml"]

dev_requires = [
    "autoflake~=1.4",
    "autopep8~=1.5",
    "black~=22.6",
    "coverage~=6.4",
    "coverage-badge~=1.0",
    "flake8~=3.9",
    "isort~=5.9",
    "pytest~=7.1",
    "pip-tools~=6.2"
]


def get_version():
    return import_module("{{ cookiecutter.project_slug }}.__version__").__version__


setup(
    name="{{ cookiecutter.project_slug }}",
    version=get_version(),
    url="https://github.com/____/{{ cookiecutter.project_slug }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=install_requires,
    setup_requires=["pytest-runner"],
    tests_require=dev_requires,
    extras_require={"dev": dev_requires},
    entry_points={"console_scripts": ["{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.main:main"]},
)
