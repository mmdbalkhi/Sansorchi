from setuptools import setup

from version import __VERSION__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="Sansorchi",
    packages=["Sansorchi"],
    version=__VERSION__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Remove Persian (Farsi) Swear Words",
    author="KomeilParseh",
    author_email="ahmdparsh129@gmail.com",
    url="https://github.com/KomeilParseh/Sansorchi",
    download_url="https://github.com/KomeilParseh/Sansorchi",
    keywords=["Improper words", "swearing", "sansorchi", "Sansorchi"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
