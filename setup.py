import os
from setuptools import setup, find_packages

with open("readme.md", "r") as fh:
    long_description = fh.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="kkiapay",
    version="0.0.6",
    author="Junior Gantin",
    author_email="nioperas06@gmail.com",
    description="Community-driven Admin KkiaPay Sdk for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PythonBenin/kkiapay-python",
    packages=[p for p in find_packages('.', exclude=['tests'])],
    install_requires=[
        'requests==2.24.0',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
