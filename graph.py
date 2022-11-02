import matplotlib as mpl
import numpy as np


class TiterGraph: # creates a scatter plot and line of best fit to visualize and calculate titer concentration
    def DNAdf(self):
        # TODO: create a data frame that represents the concentration of AAV titer DNA
        DNAdf = [100, 50, 25, 12.5, 6.25, 3.125, 1.56, 0.39, 0.2, 0.1, 0]
        return DNAdf


    def measureDNAdf(self, absorbance):
        # TODO: create a data frame that imports measured concentration from excel file
        absorbancedf = [absorbance]
        return absorbancedf


    def lobf(self, aavSTD, absorance):
        # TODO: create a line of best fit which is appended to the graph(matplotlib probably has this function)
        return
    def showgraph(self, aavSTD, absorbance):
        # TODO: display the graph with lobf
        return
