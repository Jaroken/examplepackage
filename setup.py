from setuptools import setup, find_packages

setup(
    name = 'examplepackage',
    version = "0.0.1",
    author = "KP",
    description = "Just a dummy project that can be pip installed and conda installed",
    packages = find_packages(),
    install_requires = [
        'pandas >=1.4'],
    python_requires = '>=3.5'
)