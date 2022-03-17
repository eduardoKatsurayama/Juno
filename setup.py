from re import search
from setuptools import find_packages, setup

with open('README.md') as f:
    README = f.read()

with open('requirements/prod.txt') as f:
    dependencies = f.read().splitlines()

with open('cyrodiil/__init__.py') as f:
    version = search(r"version = \'(.*)\'", f.read()).group(1)

with open('requirements/dev.txt') as f:
    tests = f.read().splitlines()[2:]

setup(
    name='cyrodiil',
    url='https://github.com/eduardoKatsurayama/cyrodiil.git',
    author=['Eduardo Katsurayama'],
    author_email='eduardoabreu.db@gmail.com',
    packages=find_packages(),
    install_requires=dependencies,
    version=version,
    description=(
        'Cyrodiil is a library that abstracts Riot Games API requests'
    ),
    long_description=README,
    tests_require=tests,
)
