from setuptools import setup, find_packages

with open("README.md", "r") as f:
  page_description = f.read()

with open("requirements.txt") as f:
  requirements = f.read().splitlines()

setup(
  name="package_name",
  version="0.0.1",
  author="Vivs15",
  author_email="koscak100@gmail.com",
  description="Meu primeiro pacote",
  long_description=page_description,
  long_description_content_type="meu primeiro pacote",
  url:"https://github.com/Vivs15/image-processing-package/edit/master/setup.py"
  packages=find_packages(),
  install_requires=requirements,
  python_requires=':=3.8',
)
