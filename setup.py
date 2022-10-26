from distutils.core import setup
setup(
  name = 'SeCreepy',
  packages = ['secreepy'],
  version = '0.3.0',
  license='MIT',
  description = 'A wrapper for undetected chromedriver that works perfectly for long-running scrapping',
  author_email = 'fadi.younes.syr@gmail.com',
  url = 'https://github.com/repeating/secreepy',
  download_url = 'https://github.com/repeating/secreepy/archive/v0.3.0.tar.gz',
  keywords = ['Selenium', 'undetected chromedriver', 'Web Scrapping'],
  install_requires=[            # I get to this in a second
          'selenium',
          'undetected-chromedriver',
          'urllib3',
          'psutil'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
