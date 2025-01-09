from setuptools import setup, find_packages


setup(
    name="scopium",
    version="1.0.0-alpha",
    author="Khaled Mahmoud Al Jamous",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/khxql/Scopium",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "webdriver-manager"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Development Status :: 3 - Alpha"
    ]
)