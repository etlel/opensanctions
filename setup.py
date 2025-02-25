from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()


setup(
    name="opensanctions",
    version="3.2.0",
    url="https://opensanctions.org",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="OpenSanctions",
    author_email="info@opensanctions.org",
    packages=find_packages(exclude=["ez_setup", "examples", "test"]),
    namespace_packages=[],
    package_data={
        "opensanctions": [
            "*.yml",
            "*.yaml",
            "*.ini",
            "*.mako",
            "*.ijson",
            "migrate/versions/*.py",
        ]
    },
    zip_safe=False,
    install_requires=[
        "followthemoney >= 3.2.0",
        "nomenklatura >= 2.7.5, < 3.0.0",
        "orjson == 3.8.6",
        "zavod >= 0.5.0",
        "pantomime",
        "sqlalchemy[mypy]",
        "requests[security]",
        "types-requests",
        "psycopg2-binary",
        "certifi",
        "addressformatting",
        "prefixdate",
        "datapatch",
        "structlog",
        "colorama",
        "pyicu < 2.11.0",
        "openpyxl == 3.1.0",
        "xlrd",
        "lxml",
        "lxml-stubs",
        "awscli",
    ],
    extras_require={
        "dev": [
            "sphinx",
            "bump2version",
            "wheel>=0.29.0",
            "twine",
            "black",
            "flake8>=2.6.0",
            "sphinx-rtd-theme",
        ],
    },
    entry_points={
        "console_scripts": [
            "opensanctions = opensanctions.cli:cli",
            "osanc = opensanctions.cli:cli",
        ],
    },
)
