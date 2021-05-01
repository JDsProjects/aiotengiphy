from setuptools import setup
import re

with open('aiotengiohy/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open("README.md", "r") as f:
    long_description = f.read()

setup(
  name = 'aiotengiphy',
  packages = ['aiotengiphy'],
  version = version, 
  license='MIT', 
  description = 'An async wrapper for Tenor and Giphy',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'JDJGIncOfficial',
  author_email = 'jdjgbot@gmail.com',
  url = 'https://github.com/JDJGInc/aiotengiphy,
  download_url = 'https://github.com/JDJGInc/tenorgiphy,',
  keywords = ['wrapper', 'api', 'random'],
  install_requires=['aiohttp','yarl'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ], 
) 
