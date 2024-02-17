import importlib.metadata

import pytest

import app


@pytest.mark.e2e()
def test_luda_version() -> None:
    """Test that the version is the same as in pyproject.toml."""
    assert app.__version__ == importlib.metadata.version(app.__name__)
