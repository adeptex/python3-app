from datetime import datetime
from pathlib import Path

import pytest
from yaml import safe_load

from {{cookiecutter.project_slug}}.utils import load_json_file, load_yaml_file, today


def test_today():
    result = today().split("-")[0]
    expected = str(datetime.now().year)
    assert result == expected


def test_load_json_from_file():
    fixture = Path(__file__).parent.joinpath("../fixtures/fixture.json")
    result = load_json_file(fixture)
    expected = {"project": "cookie"}
    assert result == expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    [(None, {}), ("tests/fixtures/config.yml", safe_load(open("tests/fixtures/config.yml")))],
)
def test_load_yaml_file(filename, expected):
    result = load_yaml_file(filename)
    assert result == expected
