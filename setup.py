from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='pyboon',  # 包名
      version='0.0.19',  # 版本号
      description='A boon',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='east196',
      author_email='east196@outlook.com',
      url='https://github.com/east196/pyboon',
      install_requires=['requests', 'bs4', 'rich',
                        'chevron', 'markdown', 'pyyaml'],
      license='Apache License 2.0',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries'
      ],
      )
