#!/usr/bin/env python
# pylint: disable=C0326

from setuptools import setup, find_packages

# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = ['Development Status :: 3 - Alpha',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(
    name             = 'unicorn_client',
    version          = '1.0.0',
    author           = 'Pierre Cavan',
    author_email     = 'ammonite.myfox@gmail.com',
    description      = """Unicorn client""",
    long_description = """Unicorn client""",
    license          = 'MIT',
    keywords         = 'Raspberry Pi',
    url              = 'https://github.com/amm0nite',
    classifiers      = CLASSIFIERS,
    packages         = find_packages(),
    install_requires = [],
    entry_points     = {'console_scripts': ['unicorn_client=unicorn_client:main']}
)


# https://packaging.python.org/
# http://peterdowns.com/posts/first-time-with-pypi.html
# https://github.com/pimoroni/unicorn-hat/tree/master/library/UnicornHat
# https://github.com/pypa/sampleproject
