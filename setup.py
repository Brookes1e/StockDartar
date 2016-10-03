from setuptools import setup,find_packages

setup(name='Stock Darttar',
      version='1.0',
      packages=find_packages(),
      author='Harry Brookes',
      author_email='harrybrookes@hotmail.co.uk',
      scripts=['__main__.py','stock_class.py','graph.py'],
      license='MIT',
      description='Yahoo finance stock scraper',
      long_description="Stock Dartar is a object orientated program that allows the user to download and look at any stock that is in Yahoo's database, the Yahoo API is used for the scraper's interaction with the database"
      )
