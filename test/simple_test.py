import os

"""This bash script provides an example of the command line code that should, this example provides the open and close
of the IBM stock on each day of the 2015/16 financial year"""

os.system("python ../../StockDartar -S 'IBM' -s '2015-4-1' -e '2016-3-31' -p close open")
