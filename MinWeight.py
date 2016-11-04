"""
@author: Angus Whitehead
"""
import Strategy


class MinWeight(Strategy.Strategy):

    def show_results(self, stat):
        print("the lightest pokemon you have got data on is " + stat[0]
              + " at only " + str(stat[1]) + "kg")
