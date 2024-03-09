from contextlib import contextmanager

import pytest


@contextmanager
def does_not_raise():
    yield


@pytest.fixture
def config_fixture():
    return open("tests/fixtures/fixture.json").read()
