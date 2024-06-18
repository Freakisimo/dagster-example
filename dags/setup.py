from setuptools import find_packages, setup


setup(
    name='dags',
    packages=find_packages(exclude=['tests'])
)