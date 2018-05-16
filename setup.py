# setup.py
from setuptools import setup, find_packages
import meta
dependencies = [
    'dask','xarray',
]
setup(
    name = meta.name,
    version = meta.version,
    packages = find_packages(),
    install_requires = dependencies,
    author = meta.author,
    # ...
    )
