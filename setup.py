#!/usr/bin/env python

import subprocess
import sys

try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        extra_kwargs = {'tests_require': ['pytest', 'mock']}

        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            import pytest
            sys.exit(pytest.main(self.test_args))

except ImportError:
    from distutils.core import setup, Command

    class PyTest(Command):
        extra_kwargs = {}
        user_options = []

        def initialize_options(self):
            pass

        def finalize_options(self):
            pass

        def run(self):
            raise SystemExit(subprocess.call([sys.executable, 'runtests.py']))

try:
   import pypandoc
   readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError, RuntimeError):
   readme = ''

setup(name='concentration',
      version='1.0.0',
      description="Get work done when you need to, goof off when you don't.",
      long_description=readme,
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='https://github.com/timothycrosley/concentration',
      license='MIT',
      requires=['hug'],
      install_requires=['hug>=2.0.0'],
      entry_points={
        'console_scripts': [
            'concentration = concentration.run:__hug__.cli',
        ]
      },
      packages=['concentration'],
      cmdclass={'test': PyTest},
      keywords='Focus, Python, Python2, Python3, Firewall, Filter, Utility, Concentration',
      classifiers=['Development Status :: 6 - Mature',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Environment :: Console',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.0',
                   'Programming Language :: Python :: 3.1',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Utilities'],
      **PyTest.extra_kwargs)
