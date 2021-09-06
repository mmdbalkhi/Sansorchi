from sansorchi import version

with open("README.md", encoding="utf-8") as fh:
    readme = fh.read()

dev_requires = ["black", "pytest", "pylint"]
doc_requires = ["sphinx", "myst_parser"]


def setup_package():
    metadata = dict(
        name="Sansorchi",
        packages=["sansorchi"],
        version=version,
        long_description=readme,
        long_description_content_type="text/markdown",
        description="Remove Persian (Farsi) Swear Words",
        author="KomeilParseh",
        author_email="ahmdparsh129@gmail.com",
        url="https://github.com/KomeilParseh/Sansorchi",
        download_url="https://github.com/KomeilParseh/Sansorchi/releases",
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
        python_requires=">=3.6",
        extras_require={"dev": dev_requires, "docs": doc_requires},
    )
    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
