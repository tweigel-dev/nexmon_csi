import matplotlib.pyplot as plt
import json
import math
from csi_entry import CsiEntry



def plot_ampli(csi_entry : CsiEntry):

    amplitudes = [abs(csi_comp) for csi_comp in csi_entry.csi]
    plt.plot(range(len(csi_entry.csi)), amplitudes, label="Antenna {}".format(csi_entry.rx))
    
    plt.xlabel('Subcarrier index')
    plt.ylabel('amplitude')