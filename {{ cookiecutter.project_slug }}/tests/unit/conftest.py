from contextlib import contextmanager

import pytest


@contextmanager
def does_not_raise():
    yield


@pytest.fixture
def rule_fixture():
    return {}
