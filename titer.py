import numpy as np

class Titer:
    def calculate_titer(self, hot_sample, cold_sample, slope, intercept):
        # TODO: Pass samples and calculate titer

        final = hot_sample-cold_sample

        formula = (final - intercept)/slope

        titer = (15*formula*360000000*(15/13.5))/0.01

        return titer

    def label_titers(self, titer):
        # TODO: for each sample calculated, label it with its corresponding name
        pass
