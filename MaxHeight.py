"""
@author: Angus Whitehead
"""
import Strategy


class MaxHeight(Strategy.Strategy):

    def show_results(self, stat):
        print("the tallest pokemon you have got data on is " + stat[0]
              + " at a whooping " + str(stat[1]) + "m")
