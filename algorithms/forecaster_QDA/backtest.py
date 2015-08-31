__author__ = 'vishnu'

'''
    Library holding definition to implement the backtesting Algorithm
    class Strategy
    class Portfolio
'''


from abc import ABCMeta, abstractmethod


class Strategy(object):
    """ Strategy is abstract base class providing an interface for
        all subsequent ( inherited ) trading strategies.

    the goal of the derived strategy object is to output a list of signals
    which has the form of a time series indexed pandas Dataframe.

    In this instances only a single symbol is supported
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_signals(self):
        """ An implementation is required to return the dataframe of symbols
        containing the signals to go long , short or hold (1, -1, or 0)
        :return: Implementation Error
        """
        raise NotImplementedError("Should implement method: generate_signals() ")







