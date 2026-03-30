import numpy as np
import matplotlib.pyplot as plt

#Import data
data1 = np.loadtxt('Data1.csv', delimiter=',', skiprows=1)
data2 = np.loadtxt('Data2.csv', delimiter=',', skiprows=1)
data3 = np.loadtxt('Data3.csv', delimiter=',', skiprows=1)
data4 = np.loadtxt('Data4.csv', delimiter=',', skiprows=1)
data5 = np.loadtxt('Data5.csv', delimiter=',', skiprows=1)
data6 = np.loadtxt('Data6.csv', delimiter=',', skiprows=1)
# List of Datasets
ListOfData = [data1, data2, data3, data4, data5, data6]
def normalPlot(ListOfData):
    plt.figure(figsize=(10, 6))
    plt.plot(data1[:, 0], data1[:, 1], label='Data1', marker='o')
    plt.plot(data2[:, 0], data2[:, 1], label='Data2', marker='s')
    plt.plot(data3[:, 0], data3[:, 1], label='Data3', marker='^')
    plt.plot(data4[:, 0], data4[:, 1], label='Data4', marker='d')
    plt.plot(data5[:, 0], data5[:, 1], label='Data5', marker='x')
    plt.plot(data6[:, 0], data6[:, 1], label='Data6', marker='v')


    plt.xlabel('Time [s]')
    plt.ylabel('Temperature [°C]')
    plt.title('Plot of Temperature over Time')
    plt.legend()
    plt.grid()
    plt.show()  


def normalizedPlot(ListOfData):
    # Normalize the data by subtracting the first temperature value from all temperature values
    plt.figure(figsize=(10, 6))
    for i, data in enumerate(ListOfData):
        normalized_temperature = data[:, 1] - data[0, 1]
        plt.plot(data[:, 0], normalized_temperature, label=f'Data{i+1}', marker='o')

    # Plot the normailzed data like before
    plt.xlabel('Time [s]')
    plt.ylabel('Normalized Temperature [°C]')
    plt.title('Normalized Plot of Temperature over Time')
    plt.legend()
    plt.grid()
    plt.show()

normalPlot(ListOfData)
normalizedPlot(ListOfData)
