from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
)
