import pandas as pd


# the file name
fileName = ('path_of_excel_file') # TODO: add a file input

# store the new data into this variable called file Data
fileData = pd.read_excel(fileName)

fileData


def data():
    absorbance = []
    for std in len(12):
        absorbance.append(std)

    return absorbance
