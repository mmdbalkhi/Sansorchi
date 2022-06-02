from sansorchi import __version__

with open("README.md", encoding="utf-8") as fh:
    readme = fh.read()


def setup_package():
    metadata = dict(
        name="Sansorchi",
        packages=["sansorchi"],
        version=__version__,
        long_description=readme,
        long_description_content_type="text/markdown",
        description="Remove Persian (Farsi) Swear Words",
        author="KomeilParseh",
        author_email="ahmdparsh129@gmail.com",
        url="https://github.com/KomeilParseh/Sansorchi",
        download_url="https://github.com/KomeilParseh/Sansorchi/releases",
        install_requires=["hazm>=0.7.0"],
        keywords=[
            "Improper words",
            "swearing",
            "sansorchi",
            "Sansorchi",
            "سانسور",
            "سانسورچی",
            "فحش",
            "پایتون",
        ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.7",
    )
    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
