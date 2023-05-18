import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import functions
import statistics


data = input("Please Enter File name with extension: ") #TODO: change this and line 32 to be taken in from the gui 
samples = int(input("Please Enter number of samples: "))
exceldata = pd.read_excel(data)
df = pd.DataFrame(exceldata)


##################################################################################################
DNAdf = [100, 50, 25, 12.5, 6.25, 3.125, 1.56, 0.78, 0.39, 0.195, 0.1, 0] #serial dilution df
dfSTD = df.iloc[0, 2:] #extracts STD data into new DF
dfHOT = df.iloc[1, 2:2+samples] #extracts hot data into new DF
dfCOLD = df.iloc[2, 2:2+samples] #extracts cold Data into new DF 
##################################################################################################
DNAdf2 = [50, 25, 12.5, 6.25, 3.125, 1.56, 0.78, 0.39, 0.195, 0.1, 0] #serial dilution for calculating based on only 11 values (calculate better r value)
dfSTD2 = df.iloc[0, 3:] #extract viral df to match with the serial dilution length
x2 = np.array(DNAdf2, dtype=np.float64) #expected DNA concentration per sample 
y2 = np.array(dfSTD2, dtype=np.float64) #actual DNA concentration per sample 
##################################################################################################
x = np.array(DNAdf, dtype=np.float64) #expected DNA concentration per sample 
y = np.array(dfSTD, dtype=np.float64) #actual values
hot = np.array(dfHOT, dtype=np.float64) #hot samples 
cold = np.array(dfCOLD, dtype=np.float64) #cold samples 
diff = []
##################################################################################################


def rSquared(act_results, expected_results, slope, intercept): #function that determines the r square value
    ss_error = 0 #sum squared error 
    ss_tot = 0 #sum squared total
    for i in enumerate(y-1): 
        ss_error += (act_results[i] - slope * expected_results[i] + intercept)**2 #from index 0 to 11 take that array value and subract the line of best fit position 
        ss_tot += ( y[i]-statistics.mean(y))**2 # for each point in the array subtract the mean from it
    r_square = round(1 - (ss_error/ss_tot), 4) # r squared = (1 - (ss_error/ss_tot)) then round to 4 decimal points
    return r_square # return the r square value 


def compareR(r1, r2): # a function that compares the r square values to determine the better
    if(r1>r2):
        return r1
    elif(r1 == r2):
        return r1
    else:
        return r2


def titer(sample_difference, slope, intercept): #function that calculates the actual titer of the virus 
    titerlist = []
    for i in enumerate(sample_difference):
        reshape = (sample_difference[i] - intercept )/slope
        titer = scientific_notation="{:e}".format((15*reshape*360000000*(15/13.5))/0.01)
        titerlist.append(titer)
        return titerlist



def calculate():
    if len(x) == len(y):
        for int in enumerate(y):
            y[int] = y[int]- y[len(y)-1] #reshapes the data by subtracting irrelevant noise from the samples

    if len(hot) == len(cold):
        for int in enumerate(hot):
            diff.append(hot[int] - cold[int]) # take the difference between hot and cold and append that difference to a list

    hcDiff = np.array(diff, dtype=np.float64) #turn the list into an np array
    slope, intercept = np.polyfit(x, y, 1)
    print(titer(hcDiff, slope, intercept)) ##TODO: change this 

calculate()

