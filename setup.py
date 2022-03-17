from setuptools import find_packages, setup

setup(
    name='cyrodiil',
    url='https://github.com/eduardoKatsurayama/cyrodiil.git',
    author=['Eduardo Katsurayama'],
    author_email='eduardoabreu.db@gmail.com',
    packages=find_packages(),
    install_requires=open('requirements/prod.txt').read().splitlines(),
    version='0.0.1',
    description=(
        'Cyrodiil is a library that abstracts Riot Games API requests'
    ),
    long_description=open('README.md').read(),
    tests_require=open('requirements/dev.txt').read().splitlines()[2:],
)
