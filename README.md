Concentration
============================
[![PyPI version](https://badge.fury.io/py/concentration.svg)](http://badge.fury.io/py/concentration)
[![Test Status](https://github.com/timothycrosley/concentration/workflows/Test/badge.svg?branch=develop)](https://github.com/timothycrosley/concentration/actions?query=workflow%3ATest)
[![Lint Status](https://github.com/timothycrosley/concentration/workflows/Lint/badge.svg?branch=develop)](https://github.com/timothycrosley/concentration/actions?query=workflow%3ALint)
[![codecov](https://codecov.io/gh/timothycrosley/concentration/branch/master/graph/badge.svg)](https://codecov.io/gh/timothycrosley/concentration)
[![Join the chat at https://gitter.im/timothycrosley/concentration](https://badges.gitter.im/timothycrosley/concentration.svg)](https://gitter.im/timothycrosley/concentration?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/concentration/)
[![Downloads](https://pepy.tech/badge/concentration)](https://pepy.tech/project/concentration)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://timothycrosley.github.io/isort/)
_________________

[Read Latest Documentation](https://timothycrosley.github.io/concentration/) - [Browse GitHub Code Repository](https://github.com/timothycrosley/concentration/)

Stay focused on work when you want, and goof off when you don't. Concentration is a simple
Python 3 console utility to block distracting sites when you need to focus, while allowing you to easily
take timed breaks. Concentration uses the /etc/hosts file as the mechanism to
block sites, and works on Linux, Macintosh, and Windows.

![Concentration Example](https://raw.github.com/timothycrosley/concentration/develop/example.gif)


Installing Concentration
============================

    pip3 install concentration

Or, if pip is already set to use Python 3

    pip install concentration

Or, if you wanted concentration installed and ran in an isolated environment, consider using [pipx](https://github.com/pipxproject/pipx):

    pipx run concentration


Using Concentration
============================

To keep focused (blocking distracting sites):

    sudo concentration improve

To take a small 5 minute timed break:

    sudo concentration break

To take a long 60 minute timed break:

    sudo concentration break -m 60

You can cancel breaks with `Ctrl-C`.

To disable blocking until you explicitly enable it again:

    sudo concentration lose


Configuring Concentration
============================

You can add more files to the blocked list by putting them in the following files (new line delimited):
- ~/.concentration.distractors
- /etc/concentration.distractors


You can make sure sites are visible even if concentration is enabled by putting them in the following files (new line delimited):
- ~/.concentration.safe
- /etc/concentration.safe

--------------------------------------------

Thanks and I hope you find concentration useful in your effort to get more done!

~Timothy Crosley
