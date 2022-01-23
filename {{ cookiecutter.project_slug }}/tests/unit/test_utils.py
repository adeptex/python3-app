from datetime import datetime
from os import remove
from pathlib import Path

import pytest

from {{cookiecutter.project_slug}}.utils import load_json_from_file, load_regex, printer, today
from tests.unit.conftest import does_not_raise


def test_today():
    result = today().split("-")[0]
    expected = str(datetime.now().year)
    assert result == expected


def test_load_json_from_file():
    fixture = Path(__file__).parent.joinpath("../fixtures/fixture.json")
    result = load_json_from_file(fixture)
    expected = {"project": "{{ cookiecutter.project_slug }}"}
    assert result == expected


@pytest.mark.parametrize(
    ("regex", "expected"), [("", does_not_raise()), ("*", pytest.raises(ValueError)), (".*", does_not_raise()),],
)
def test_load_regex(regex, expected):
    with expected:
        assert load_regex(regex)


@pytest.mark.parametrize(
    ("filepath", "expected"), [(None, False), (Path("/tmp/printer"), True),],
)
def test_printer(filepath, expected):
    result = Path("/tmp/printer")
    try:
        remove(result.as_posix())
    except (FileNotFoundError, AttributeError):
        pass

    printer("test", filepath)
    assert result.is_file() == expected

    try:
        remove(result.as_posix())
    except (FileNotFoundError, AttributeError):
        pass
