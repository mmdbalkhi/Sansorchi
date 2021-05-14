from distutils.core import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='Sansorchi',
    packages=['Sansorchi'],
    version='1.0.0',
    long_description=long_description,
    long_description_content_type="text/markdown",

    description='Sansorchi is a program to remove bad and inappropriate words',
    author='KomeilParseh',
    author_email='ahmdparsh129@gmail.com',
    url='https://github.com/KomeilParseh/Sansorchi',
    download_url='https://github.com/KomeilParseh/Sansorchi',
    keywords=['Improper words', 'swearing', "sansorchi", "Sansorchi"],
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GPL-3)',
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
