import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitcoinhisprice-leocan",
    version="0.0.1",
    author="Chen Xucan",
    author_email="chenxucan1991@gmail.com",
    description="A package to retrive bitcoin history price data from coin market cap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leoacan/bitcoinhisyprice.git",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests>=2.18.4',
        'requests_cache>=0.4.13',
        'bs4>=0.01'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)