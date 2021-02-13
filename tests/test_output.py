from unittest import mock

from concentration import output


def test_banner():
    some_height = 24
    with mock.patch("shutil.get_terminal_size", return_value=(12, some_height)):
        assert output.banner("ABCD") == "####ABCD####"
    with mock.patch("shutil.get_terminal_size", return_value=(24, some_height)):
        assert output.banner("ABCD") == "##########ABCD##########"
    with mock.patch("shutil.get_terminal_size", return_value=(2, some_height)):
        assert output.banner("ABCD") == "ABCD"
