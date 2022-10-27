import os
import sys

py_version = sys.version_info[:2]

if py_version < (3, 10):
    raise RuntimeError('42Emoji requires Python 3.10 or later')

# pkg_resource is used in several places
requires = ["setuptools"]
tests_require = []

testing_extras = tests_require + [
    'pytest',
    'pytest-cov',
]

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
version_txt = '0.0.1'

dist = setup(
    name='42emoji',
    version=version_txt,
    license='MIT',
    description="Application for moderated 42 emojis",
    author="Harm Smits",
    author_email="harmsmitsdev@gmail.com",
    packages=find_packages(),
    install_requires=requires,
    extras_require={
        'testing': testing_extras,
    },
    tests_require=tests_require,
    include_package_data=True,
    zip_safe=False,
    test_suite="src.tests",
    entry_points={
        'console_scripts': [
            '42emoji = src.42emoji:main',
        ],
    },
)