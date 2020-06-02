import os.path
import re
from setuptools import setup

(__version__, ) = re.findall("__version__.*\s*=\s*[']([^']+)[']",
                             open('hello_world/__init__.py').read())

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="hello_world",
    version=__version__,
    description="Program welcomes the world",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/octocat/Hello-World",
    author="octocat",
    author_email="hello_world_author@example.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    packages=["hello_world"],
    include_package_data=True,
    install_requires=[
        "python-dateutil>=2.7.1"
    ],
    entry_points={"console_scripts": ["hello_world=hello_world.__main__:main"]},
)
