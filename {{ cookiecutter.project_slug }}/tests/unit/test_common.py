from datetime import datetime

import pytest

from {{cookiecutter.project_slug}}.common import today


def test_today():
    result = today().split("-")[0]
    expected = str(datetime.now().year)
    assert result == expected
