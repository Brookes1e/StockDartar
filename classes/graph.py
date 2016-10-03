import pylab
import datetime
import traceback


class Graph:
    """The graph class is used to provide a graphical representations of the desired data. The class uses pylab as
    the function for its data plotting. The traceback and datetime modules are also used to provide more info about
    any bugs and to complete datetime conversions, respectively"""

    def __init__(self):
        pass

    @classmethod
    def plot(cls, dates, *data_options):
        """The plot method allows the passing of multiple price actions to the method which then plots them to the same
        graph

        Parameters
        ----------
        dates - requires the input of the dates list created in the stock_class_init__ method
        *data_options - are passed by the user at the command line using the -p option and carries the price actions
        that are desired to be plotted"""
        try:
            dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in dates]
            [pylab.plot(dates, option) for option in data_options]

        except Exception, error_Graph_show:
            print 'error_Graph_show :', error_Graph_show

    @classmethod
    def show(cls):
        """The show method requires no arguments and provide the user with the ability to call their graph when they
        have finished adding their desired data"""
        try:
            pylab.show()

        except:
            print traceback.print_exc()


