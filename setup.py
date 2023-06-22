from setuptools import setup, find_packages

setup(name="etep",
      version="0.0.1",
      author="loki",
      author_email="lokashwar@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )