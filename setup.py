from setuptools import setup, find_packages

setup(name='python_voc_parser',
      version='0.1',
      description='Python pascal voc dataset parset',
      # see: https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries'
      ],
      url='https://github.com/gabrielrezzonico/python_voc_parser',
      download_url = 'https://github.com/gabrielrezzonico/python_voc_parser/tarball/0.1',
      author='Gabriel Rezzonico',
      author_email='gabrielrezzonico@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      # $ pip install -e .[dev,test]
      extras_require={
          'dev': ['sphinx'],
          'test': ['pytest', 'pytest-cov'],
      },
      #https://packaging.python.org/requirements/
      install_requires=['pandas'],
      zip_safe=False)


