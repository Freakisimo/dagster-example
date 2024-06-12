from setuptools import find_packages, setup

setup(
    name="dags",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-webserver"
    ],
    extras_require={"dev": ["pytest"]}
)