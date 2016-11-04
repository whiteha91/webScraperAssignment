"""
@author: Angus Whitehead
"""
import Strategy


class AvgWeight(Strategy.Strategy):

    def show_results(self, stat):
        print("the average weight of pokemon you have got data on is "
              + str(stat[1]) + "kg")
