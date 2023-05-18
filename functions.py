import statistics

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