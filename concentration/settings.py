"""concentration/settings.py

Defines how the basic concentration settings get loaded.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys

from .pie_slice import *

LINUX = 0
MAC = 1
WINDOWS = 2
HOSTS_FILE = "/etc/hosts"
REDIRECT_TO = "127.0.0.1"
START_TOKEN = "## START DISTRACTORS ##"
END_TOKEN = "## END DISTRACTORS ##"
SUB_DOMAINS = ('www', 'news')
DISTRACTORS = ['ycombinator.com', 'slashdot.com', 'facebook.com', 'reddit.com', 'gawker.com', 'theverge.com',
               'techcrunch.com', 'thenextweb.com', 'wired.com', 'gizmodo.com', 'slickdeals.net',
               'mashable.com', 'digitaltrends.com', 'techradar.com', 'twitter.com', 'tumblr.com',
               'technorati.com', 'digg.com', 'buzzfeed.com', 'twitter.com', 'youtube.com', 'netflix.com',
               'iwastesomuchtime.com', 'pinterest.com', 'ebay.com', 'thepointsguy.com', 'imgur.com', 'woot.com',
               'flyertalk.com', 'instagram.com', 'medium.com', 'meetup.com']

for config_file_path in ('/etc/concentration.distractors', '~/.cocentration.distractors'):
    if os.path.isfile(config_file_path):
        with open(config_file_path) as config_file:
            DISTRACTORS.extend(config_file.readlines())

PLATFORM = LINUX
for platform in (("linux", LINUX), ("darwin", MAC), ("win32", WINDOWS)):
    if platform[0] in sys.platform:
        PLATFORM = platform[1]

RESTART_NETWORK = {LINUX: [["/etc/init.d/networking", "restart"],
                           ["/etc/init.d/nscd", "restart"],
                           ["/etc/rc.d/nscd", "restart"],
                           ["/etc/rc.d/init.d/nscd", "restart"]],
                   MAC: [["dscacheutil", "-flushcache"]],
                   WINDOWS: [["ipconfig", "/flushdns"]]}[PLATFORM]
if PLATFORM is WINDOWS:
    HOSTS_FILE = "/Windows/System32/drivers/etc/hosts"
