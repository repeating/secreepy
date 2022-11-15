from distutils.core import setup
from setuptools import find_packages

setup(
  name='SeCreepy',
  packages=find_packages(),
  version='0.5.2',
  license='MIT',
  description='A wrapper for undetected chromedriver that works perfectly for long-running scrapping',
  author_email='fadi.younes.syr@gmail.com',
  url='https://github.com/repeating/secreepy',
  download_url='https://github.com/repeating/secreepy/archive/v0.5.2.tar.gz',
  keywords=['Selenium', 'undetected chromedriver', 'Web Scrapping'],
  install_requires=[
    'selenium',
    'undetected-chromedriver',
    'urllib3',
    'psutil',
    'requests-html',
    'selenium-wire'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
