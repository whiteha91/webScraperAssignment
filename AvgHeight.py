"""
@author: Angus Whitehead
"""
import Strategy


class AvgHeight(Strategy.Strategy):

    def show_results(self, stat):
        print("the average height of pokemon you have got data on is "
              + str(stat[1]) + "m")
