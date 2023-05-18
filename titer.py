import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import functions


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




def calculate():
    if len(x) == len(y):
        for int in enumerate(y):
            y[int] = y[int]- y[len(y)-1] #reshapes the data by subtracting irrelevant noise from the samples

    if len(hot) == len(cold):
        for int in enumerate(hot):
            diff.append(hot[int] - cold[int]) # take the difference between hot and cold and append that difference to a list

    hcDiff = np.array(diff, dtype=np.float64) #turn the list into an np array
    slope, intercept = np.polyfit(x, y, 1)

    print(functions.titer(hcDiff, slope, intercept)) ##TODO: change this 
    highestR = functions.compareR(functions.rSquared(y,x,slope,intercept), functions.rSquared(y2,x2,slope,intercept))
    plt.scatter(DNAdf, dfSTD)
    plt.plot(x, slope*x+intercept) #line of best fit
    plt.title(label="R^2=" + str(highestR) + 
    ',  y = ' + '{:.2f}'.format(slope) + ' + {:.2f}'.format(intercept) + 'x' , loc='left') # TODO: use F-string
    plt.show()


