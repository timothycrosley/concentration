"""test_concentration.py

Basic testing to ensure concentration will load
"""
from concentration import run, settings


def test_run():
    assert run


def test_settings():
    assert settings.PLATFORM in (settings.OS.linux, settings.OS.mac, settings.OS.windows)
    assert settings.HOSTS_FILE and isinstance(settings.HOSTS_FILE, str)
    assert settings.DISTRACTORS and isinstance(settings.DISTRACTORS, (list, tuple, set))
