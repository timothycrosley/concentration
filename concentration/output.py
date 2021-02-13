"""concentration/settings.py

Helpers for formatting CLI output.
"""
import shutil


def banner(txt):
    width, _ = shutil.get_terminal_size()
    return txt.center(width, "#")
