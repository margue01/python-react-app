from setuptools import setup, find_packages

with open("requirements.txt") as requirements:
    REQUIREMENTS = requirements.readlines()

for line in open("app_people/__init__.py"):
    if line.startswith("__version__ ="):
        exec(line)

setup(
    name="app_people",
    version=globals()["__version__"],
    author="Martin Guest",
    author_email="guest.martin@gmail.com",
    url="",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    test_requires=[],
    test_suite="tests"
)
