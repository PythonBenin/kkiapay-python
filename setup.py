import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kkiapay",
    version="0.0.1",
    author="Junior Gantin",
    author_email="nioperas06@gmail.com",
    description="Community-driven Admin KkiaPay Sdk for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PythonBenin/kkiapay-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
