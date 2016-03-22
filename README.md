Concentration
============================
[![Join the chat at https://gitter.im/timothycrosley/concentration](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/timothycrosley/concentration?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Stay focused on work when you want, and goof off when you don't. Concentration is a simple
Python 3 console utility to block distracting sites when you need to focus, while allowing you to easily
take timed breaks. Internally uses /etc/hosts file as the mechanism to block sites.

[Concentration Example](https://raw.github.com/timothycrosley/concentration/develop/example.gif)


Installing Concentration
============================

    pip3 install concentration

    # Or if pip is already set to use Python 3
    pip install concentration


Using Concentration
============================

To keep focused (blocking distracting sites):

    sudo concentration improve

To take a small 5 minute timed break:

    sudo concentration break

To take a long 60 minute timed break:

    sudo concentration break -m 60

To access all sites:

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
