# How it works:
# 1. Load Data from CSV files
# 2. Make List of Datasets
# 3. Make 2 functions, one for normal plot and one for normalized plot
# 4. Call the functiuons to display plots 

import os
import numpy as np
import matplotlib.pyplot as plt

DATA_DIR = os.path.dirname(__file__)

#Import data
data1 = np.loadtxt(os.path.join(DATA_DIR, 'Data1.csv'), delimiter=',', skiprows=1)
data2 = np.loadtxt(os.path.join(DATA_DIR, 'Data2.csv'), delimiter=',', skiprows=1)
data3 = np.loadtxt(os.path.join(DATA_DIR, 'Data3.csv'), delimiter=',', skiprows=1)
data4 = np.loadtxt(os.path.join(DATA_DIR, 'Data4.csv'), delimiter=',', skiprows=1)
data5 = np.loadtxt(os.path.join(DATA_DIR, 'Data5.csv'), delimiter=',', skiprows=1)
data6 = np.loadtxt(os.path.join(DATA_DIR, 'Data6.csv'), delimiter=',', skiprows=1)
# List of Datasets
ListOfData = [data1, data2, data3, data4, data5, data6]
ListOflabels = ['Benzoic acid', 'Benzoic acid', 'Fumaric acid', 'Maleic acid', 'Fumaric acid', 'Maleic acid']
def normalPlot(ListOfData, ListOflabels):
    plt.figure(figsize=(10, 6))
    for data, label in zip(ListOfData, ListOflabels):
        plt.plot(data[:, 0], data[:, 1], label=label, marker='o')
    plt.xlabel('Time [s]')
    plt.ylabel('Temperature [°C]')
    plt.title('Plot of Temperature over Time')
    plt.legend()
    plt.grid()
    plt.show()


def normalizedPlot(ListOfData, ListOflabels):
    plt.figure(figsize=(10, 6))
    for data, label in zip(ListOfData, ListOflabels):
        plt.plot(data[:, 0], data[:, 1] - data[0, 1], label=label, marker='o')

    # Plot the normailzed data like before
    plt.xlabel('Time [s]')
    plt.ylabel('Normalized Temperature [°C]')
    plt.title('Normalized Plot of Temperature over Time')
    plt.legend()
    plt.grid()
    plt.show()

normalPlot(ListOfData, ListOflabels)
normalizedPlot(ListOfData, ListOflabels)
