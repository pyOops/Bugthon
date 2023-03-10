# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:27:14 2021

@author: swb
"""

from operator import itemgetter


def read_offs(filename):
    """

    Input Parameters
    ----------
    filename : full file name of the offset file
                default location is current folder

    Returns
    -------
    Returns a list of data for each station in the ship
    Each station is a list of data representing a section
    Each station list contains tuples representing the x, y and z coordinates
        of the points that make up a section

    EXAMPLE
    -------

    data = read_offs(filename)
    data[0]

    [(-5.329, 0.0, 0.885),
     (-5.329, 0.0, 0.887),
     (-5.329, 0.015, 0.902),
     (-5.329, 0.018, 0.906),
     (-5.329, 0.031, 0.92),
     (-5.329, 0.035, 0.924),
     (-5.329, 0.047, 0.938),
     (-5.329, 0.053, 0.944),
     (-5.329, 0.063, 0.955)]

    This is a list of tuples for each data point in the first station
    """
    f = open(filename)  # Open the offset file
    tempdata = f.readlines()
    f.close()  # Close the offset file

    tempdata = [line.split("\t") for line in tempdata]  # Split lines by tabs
    if float(tempdata[0][1])-float(tempdata[30][1]) > 0.0:
        tempdata.reverse()  # Reverse data if ordered incorrectly

# Collect all the the station positions
    stns = []
    for line in tempdata:
        if float(line[1]) not in stns:
            stns.append(float(line[1]))
        else:
            continue

# Loop through all the statns to get the y and z data
    dataosb = []
    for i in range(len(stns)):
        stndata = []
        for line in tempdata:
            if float(line[1]) == stns[i]:  # Collect the y and z positions
                stndata.append((stns[i], float(line[2]), float(line[3])))
            else:
                continue
        stndata.sort(key=itemgetter(2))  # sort the data with respect to z-pos
        dataosb.append(stndata)
    return dataosb  # Return a full set of data for the ship

def plot_sections(data):
    """Takes in a list of lists representing x,y,z and plots y and z 
    for a selected station"""
    import matplotlib.pyplot as plt
    maxstn = len(data)
    a = input(f"Please select a station between 0 and {maxstn-1}: ")
    try:
        assert int(a)
    except ValueError:
        print ("This is not a number")
    else:

        a = int(a)
        xdata = [pnts[1] for pnts in data[a]]
        ydata = [pnts[2] for pnts in data[a]]
        plt.figure()
        plt.plot(xdata, ydata, '*')
        plt.axis("equal")
        plt.title('Remember to CLOSE this figure')
        plt.xlabel('Offset data (m)')
        plt.ylabel('Waterline (m)')
        
        return plt.show()

def plot_bonjeans(all_ba, all_bh, all_bv):
    """This function uses the data from create bonjeans function and plots the 
    bonjean curves for a selected station"""
    import matplotlib.pyplot as plt

    maxstn = len(all_ba)
    a = input(f"Please select a station between 0 and {maxstn-1}: ")
    try:
        assert type(a) == str
    except ValueError:
        print ("This is not a number")
    else:
        a = int(a)
        wl = [i[1] for i in all_ba[a]]
        ba = [i[0] for i in all_ba[a]]
        bv = [i[0] for i in all_bv[a]]
        bh = [i[0] for i in all_bh[a]]
        plt.figure(10, figsize=(80, 60))
#        pylab.title('Bonjean data for section: ', a)
        plt.title
        plt.subplot(131)

        plt.plot(ba, wl, '-o')
        plt.xlabel('Bonjean Area (sq.m)')
        plt.ylabel('Waterline (m)')
        plt.subplot(132)
        plt.plot(bh, wl, '-o')
        plt.xlabel('Bonjean Horizontal Moment (sq.m.m)')
        plt.ylabel('Waterline (m)')
        plt.subplot(133)
        plt.plot(bv, wl, '-o')
        plt.xlabel('Bonjean Vertical Moment (sq.m.m)')
        plt.ylabel('Waterline (m)')
        plt.show()
