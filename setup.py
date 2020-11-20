"""
setup.py for soomer
"""
#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
  name='soomer',
  version='0.0.1',
  license='GPLv3',
  description='65000 years of shitposting.',
  author='Thicculi',
  author_email='gprozendal@gmail.com',
  url='https://github.com/highlyprofessionalusername/Soomer',
  keywords=['discord', 'bot', 'meme', 'project'],
  classifiers=[
    'Development Status :: 1 - Planning',
    'Intended Audience :: End Users/Desktop',
    'Topic :: Communications :: Chat',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3.8',
  ],
  packages=find_packages(),
  include_package_data=True,
  install_requires=[
    'discord',
  ],
)
