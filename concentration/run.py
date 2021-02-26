#!/usr/bin/env python
"""Concentration

A very simple command line application to maintain focus by blocking distracting sites.
"""
import codecs
import subprocess  # nosec
import sys
import time

import hug

from . import output, settings


def reset_network(message):
    """Resets the users network to make changes take effect"""
    for command in settings.RESTART_NETWORK:
        try:
            subprocess.check_call(command)  # nosec
        except Exception:  # nosec
            pass
    print(message)


@hug.cli()
def improve():
    """Disables access to websites that are defined as 'distractors'"""
    with open(settings.HOSTS_FILE, "r+") as hosts_file:
        contents = hosts_file.read()
        if settings.START_TOKEN not in contents and settings.END_TOKEN not in contents:
            hosts_file.write(settings.START_TOKEN + "\n")
            for site in set(settings.DISTRACTORS):
                hosts_file.write("{0}\t{1}\n".format(settings.REDIRECT_TO, site))
                for sub_domain in settings.SUB_DOMAINS:
                    hosts_file.write(
                        "{0}\t{1}.{2}\n".format(settings.REDIRECT_TO, sub_domain, site)
                    )
            hosts_file.write(settings.END_TOKEN + "\n")

    reset_network("Concentration is now improved :D!")


@hug.cli()
def lose():
    """Enables access to websites that are defined as 'distractors'"""
    changed = False
    with open(settings.HOSTS_FILE, "r") as hosts_file:
        new_file = []
        in_block = False
        for line in hosts_file:
            if in_block:
                if line.strip() == settings.END_TOKEN:
                    in_block = False
                    changed = True
            elif line.strip() == settings.START_TOKEN:
                in_block = True
            else:
                new_file.append(line)
    if changed:
        with open(settings.HOSTS_FILE, "w") as hosts_file:
            hosts_file.write("".join(new_file))

    reset_network("Concentration is now lost :(.")


@hug.cli("break")
def take_break(minutes: hug.types.number = 5, now: bool=False):
    """Enables temporarily breaking concentration"""
    if not now:
        print("")
        print(output.banner("ARE YOU SURE?"))
        try:
            for remaining in range(60, -1, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds to change your mind. ".format(remaining))
                sys.stdout.write("Won't you prefer programming? Or a book?")
                sys.stdout.flush()
                time.sleep(1)
        except KeyboardInterrupt:
            print("")
            print("")
            print(":D :D :D\nGood on you! <3")
            return

    # The user insisted on breaking concentration.
    lose()
    print("")
    print(output.banner("TAKING A BREAK"))
    try:
        for remaining in range(minutes * 60, -1, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining without concentration.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(
            "\rEnough distraction!                                                            \n"
        )
        print(output.banner("BREAK OVER :)"))
        print("")
        improve()


@hug.cli()
def blocked():
    """Returns the configured list of blocked sites"""
    return settings.DISTRACTORS


@hug.cli("64")
def game():
    """Basic game implementation"""
    print(codecs.encode("Sbe Nznaqn, gur ybir bs zl yvsr", "rot_13"))
