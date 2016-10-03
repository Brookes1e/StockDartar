import yahoo_finance


class StockClass:
    """The stock class provides method to download and mamnipulate the stock data to the user's requirements.txt. The
    class will also hold the data via the use of pickle files and allow for graphical representation of the data."""

    def __init__(self, stock, start_date, end_date):
        """The init of this class converts all of the downloaded data into usable lists which can then be analysed or
        plotted through the use of other functions and modules
        """
        try:
            self.data = yahoo_finance.Share(stock).get_historical(start_date, end_date)
            self.close = [dic['Close'] for dic in self.data]
            self.open = [dic['Open'] for dic in self.data]
            self.date = [dic['Date'] for dic in self.data]
        except Exception, error_StockClass__init__:
            print 'error_StockClass__init__: ', error_StockClass__init__

    def __delete__(self):
        """The delete method has yet to be designed. NOT IN USE"""
        pass
