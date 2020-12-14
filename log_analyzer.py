import numpy as np

# function to load data from file
def loadData(filename):
    readings = {}   # dictionary to hold readings for each device
    actual = {}     # dictionary to hold actual reference values of temperature and humidity

    # open the datafile
    with open(filename, 'r') as dataFile:
        
        # read the data file line by line
        for line in dataFile:

            # split the line
            data = line.strip().split()
            
            # if this is reference line
            if data[0] == 'reference':
                # populate actual values and continue to next line
                actual['temp'] = float(data[1])
                actual['hum'] = float(data[2])
                continue
            
            # if this is device id
            if data[0] in ('thermometer', 'humidity'):
                # add device to readings and continue to next line
                device = data[1]
                if device not in readings: 
                    readings[device] = []   # list to hold measurement values of specific device
                continue
            
            # the line is a measurement, add its data to readings list
            readings[device].append(float(data[1]))

    # return actual values and readings dictionary
    return actual, readings

# function to classify / brand the devices as per standards
def classify(actual, readings):

    # empty dictionay to hold the branded devices 
    branding = {}

    # loop each device in radings dictionary
    for device in readings:

        # measurement values of the device
        data = readings[device]

        if device[:3] == 'tem':
            # device is a thermometer
            m = np.mean(data)   # mean of the data
            s = np.std(data)    # standard deviation

            # rate the thermometer
            if abs(actual['temp'] - m) > 0.5 or s>=5:
                rating = 'precise'
            else:
                if s < 3: 
                    rating = 'ultra-precise'
                else: 
                    rating =  'very-precise'
        
        else:
            # device is a humidity checker
            rating = 'keep' # start with keep
            for value in data:
                # read each value in data
                if abs(actual['hum'] - value) / actual['hum'] > 0.01: 
                    # value deviate more than 1%, discard
                    rating = 'discard'
                    break   # no need to compare further values
        
        # add device rating to branding dictionary
        branding[device] = rating
    
    # return branding dictionary 
    return branding

# call load data to get actual values and readings dictionaries
actual, readings = loadData('data.log')

# call classify to brand the devices as per standard
branding = classify(actual, readings)

# print the results
print(branding)
