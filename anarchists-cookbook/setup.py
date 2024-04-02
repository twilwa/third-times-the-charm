from setuptools import find_packages, setup

setup(
    name="anarchists_cookbook",
    packages=find_packages(exclude=["anarchists_cookbook_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "praw",
        "pandasai",
        "matplotlib",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
