
import numpy
import pylab


import stock_class


class Indicators():
    """A metaclass for all of the indicators that can be applied to the data

    """
    @classmethod
    def moving_average(cls, date, period, *data_options):
        ret = [numpy.cumsum(numpy.asarray(price, dtype=float)) for price in data_options]
        ret[period:] = ret[period:] - ret[:-period]
        pylab.plot(date, ret[period - 1:] / period)




