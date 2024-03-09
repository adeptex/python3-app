from contextlib import contextmanager

import pytest
from yaml import safe_load


@contextmanager
def does_not_raise():
    yield


@pytest.fixture
def config_fixture():
    return safe_load(open("tests/fixtures/fixture.json"))
