from setuptools import setup, find_packages

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Python generator project'

setup(
    name = 'pynumbat',
    packages = ['pynumbat'],
    entry_points={"console_scripts": ["pynumabt=pynumabt.__main__:main"]},
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = 'Eduardo Ismael Garcia Perez',
    author_email = 'eduardo78d@gmail.com',
    url = 'https://github.com/eduardogpg/pygenerate',
    keywords = ['Python Generate', 'Generate', 'Project'],
    install_requires=[ 
        'click',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)