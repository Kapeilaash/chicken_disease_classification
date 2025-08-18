from setuptools import setup, find_packages

setup(
    name="cnnClassifier",
    version="0.1.0",
    description="Chicken disease classification package",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
