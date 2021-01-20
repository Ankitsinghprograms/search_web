import setuptools

with open("README.md") as fh:
    l = fh.read()

setuptools.setup(
    name='search_web',
    version="0.1.5",
    author="Ankit Singh",
    author_email="ankitsingh300307@gmail.com",
    description="This module will Help You to Search on Different Websites like Google,Youtube,etc. By Just 2 lines Of Code",
    long_description=l,
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