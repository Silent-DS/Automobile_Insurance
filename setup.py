from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    description="An MLOps project for productionizing models",
    author="Silent-DS",
    packages=find_packages(where="src"),
    install_requires=open('requirements.txt').read().splitlines(),
)
