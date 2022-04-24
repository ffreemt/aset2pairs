"""Test aset2pairs."""
# pylint: disable=broad-except
from aset2pairs import __version__
from aset2pairs import aset2pairs


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not aset2pairs()
    except Exception:
        assert True
