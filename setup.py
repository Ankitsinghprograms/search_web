import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name='search_web',
    version="0.0.1",
    author="Ankit Singh",
    author_email="ankitsingh300307@gmail.com.com",
    description="This module will Help You to Search on Different Websites like Google,Youtube,etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ankitsinghprograms/search_web",
    install_requires=[],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)