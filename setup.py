from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='preparation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "regex"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Avisheak Das',
    author_email='avisheak.cse@std.cu.ac.bd',
    url='https://github.com/avisheak/preparation',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
