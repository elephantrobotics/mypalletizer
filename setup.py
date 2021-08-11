# encoding=utf-8
import sys

PYTHON_VERSION = sys.version_info[:2]
if (2, 7) != PYTHON_VERSION < (3, 5):
    print("This version requires Python2.7, 3.5 or later.")
    sys.exit(1)

import setuptools

import mypalletizer


if PYTHON_VERSION == (2, 7):
    long_description = ""
else:
    long_description = (
        open("README.md", encoding="utf-8").read()
        + open("docs/README.md", encoding="utf-8").read()
    )

setuptools.setup(
    name="mypalletizer",
    version=mypalletizer.__version__,
    author=mypalletizer.__author__,
    author_email=mypalletizer.__email__,
    description="Python API of serial communication for MyPalletizer series.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=mypalletizer.__git_url__,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pyserial"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, != 3.4.*",
)
