"""For pip."""

from setuptools import setup, find_packages

exec(open('numbskull/version.py').read())
setup(
    name='numbskull',
    version=__version__,
    description='sample away',
    packages=find_packages(),
    install_requires=['future'],
    entry_points={
        'console_scripts': [
            'numbskull = numbskull.numbskull:main',
        ],
    },
)
