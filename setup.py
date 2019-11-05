#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""
import os

from setuptools import setup, find_packages


setup_requires = []
setup_requires.append('pytest-runner==5.1')

cmd_class = {}
setup_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(setup_dir, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(os.path.join(setup_dir, 'CHANGELOG.rst'), encoding='utf-8') as history_file:
    history = history_file.read()

with open(
    os.path.join(setup_dir, 'blackjack_simulator', 'VERSION'), 'r', encoding='utf-8'
) as vf:
    version = vf.read().strip()


def parse_requirements_txt(filename='requirements.txt'):
    with open(os.path.join(setup_dir, filename)) as requirements_file:
        requirements = requirements_file.readlines()
        # remove whitespaces
        requirements = [line.strip().replace(' ', '') for line in requirements]
        # remove all the requirements that are comments
        requirements = [line for line in requirements if not line.startswith('#')]
        # remove empty lines
        requirements = list(filter(None, requirements))
        return requirements


setup(
    name='blackjack_simulator',
    description="Simulator for testing blackjack strategies",
    version=version,
    author="Felipe Gonzalez",
    author_email='gonzalezz_felipe@hotmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=parse_requirements_txt(),
    extras_require={
        'dev': parse_requirements_txt('requirements-dev.txt'),
        'dev-strict': [
            req.replace('>=', '==') for req in parse_requirements_txt('requirements-dev.txt')
        ],
    },
    license='MIT license',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    package_data={
        '': ['*.pxd', '*.pyx'],
        'blackjack_simulator': ['VERSION'],
    },
    data_files=[
        ('', ['requirements.txt', 'requirements-dev.txt', 'CHANGELOG.rst'])
    ],
    packages=find_packages(include=['blackjack_simulator']),
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=['pytest==4.6.3', ],
    url='https://github.com/gonzalezzfelipe/blackjack_simulator',
    zip_safe=False,
)
