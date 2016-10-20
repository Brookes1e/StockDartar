import argparse
import traceback

import classes.graph
import classes.stock_class
import classes.indicators
import GUI.GUI


def main():
    """Main function that is run from the start of the program, this includes the evaluation of arguments"""

    try:
        GUI.MyApp()
        # parser = argparse.ArgumentParser(description='Provides stock data and analysis')
        # parser.add_argument(
        #                     '--Indicators',
        #                     '-I',
        #                     type = str,
        #                     nargs = '+',
        #                     help = 'select the indicators to be used',
        #                     )
        #
        # required_args = parser.add_argument_group('Required arguments')
        # required_args.add_argument(
        #                            '--Symbols',
        #                            '-S',
        #                            type=str,
        #                            nargs='+',
        #                            help='Identifies the Yahoo finance symbol of the stock',
        #                            required=True
        #                            )
        # required_args.add_argument(
        #                            '--Start_Date',
        #                            '-s',
        #                            metavar='-s',
        #                            type=str,
        #                            help='Start date of the stock',
        #                            required=True
        #                            )
        # required_args.add_argument(
        #                            '--End_Date',
        #                            '-e',
        #                            type=str,
        #                            help='End date of the stock',
        #                            required=True
        #                            )
        #
        # required_args.add_argument(
        #                            '--Price_Actions',
        #                            '-p',
        #                            type=str,
        #                            nargs='+',
        #                            help='Price Actions of the specific stock',
        #                            required=True
        #                            )
        # args = parser.parse_args()

        # for stock_main in args.Symbols:
        #     data_main = classes.stock_class.StockClass(stock_main, args.Start_Date, args.End_Date)
        #     [classes.graph.Graph.plot(data_main.date, getattr(data_main, price_action)) for price_action in args.Price_Actions]
        #     [classes.indicators.Indicators.moving_average(data_main.date, getattr(data_main, price_action)) for price_action in args.Price_Actions]
        #     classes.graph.Graph.show()
    except:
        print traceback.print_exc()


if __name__ == '__main__':
    main()
