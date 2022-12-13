from pathlib import Path
from setuptools import find_namespace_packages, setup

# Load packages from requirement.txt file
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirement.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

# Define Package
setup(
    name="product_type", 
    version="0.1",
    description="Determine the product category the company sells based on its About Us page.",
    author="Prashant Shinde",
    author_email="mr.pshinde@gmail.com",
    url="",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
)