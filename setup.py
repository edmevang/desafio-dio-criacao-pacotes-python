from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="sales",
    version="0.0.5",
    author="Edmilson",
    #author_email="my_email",
    description="Shows increased or reduced prices.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edmevang/desafio-dio-criacao-pacotes-python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)