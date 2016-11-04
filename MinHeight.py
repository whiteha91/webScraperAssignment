"""
@author: Angus Whitehead
"""
import Strategy


class MinHeight(Strategy.Strategy):

    def show_results(self, stat):
        print("the shortest pokemon you have got data on is " + stat[0]
              + " at only " + str(stat[1]) + "m")
