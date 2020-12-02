
import matplotlib
import json



class CsiEntry( json.JSONDecoder):
    """docstring for CsiEntry"""
    def __init__(self):
        super(CsiEntry, self).__init__()
        self.correct = True
        self.code = None
        self.bfee_count = None
        self.Nrx = None
        self.Ntx = None
        self.rssiA = None
        self.rssiB = None
        self.rssiC = None
        self.noise = None
        self.agc = None
        self.antenna_sel = None
        self.length = None
        self.rate = None
        self.rssiA_db = None
        self.rssiB_db = None
        self.rssiC_db = None
        self.csi = None
        self.perm = None
        self.csi_pwr = None
        self.rssi_pwr_db = None
        self.rssi_pwr = None
        self.scale = None
        self.noise_db = None
        self.quant_error_pwr = None
        self.total_noise_pwr = None

    @classmethod
    def from_dict(cls, csi_dict):
        """
        init from json
        """
        csiEntry = cls()
        csiEntry.code = csi_dict["code"]
        csiEntry.bfee_count = csi_dict["bfee_count"]
        csiEntry.Nrx = csi_dict["Nrx"]
        csiEntry.Ntx = csi_dict["Ntx"]
        csiEntry.rssiA = csi_dict["rssiA"]
        csiEntry.rssiB = csi_dict["rssiB"]
        csiEntry.rssiC = csi_dict["rssiC"]
        csiEntry.noise = csi_dict["noise"]
        csiEntry.agc = csi_dict["agc"]
        csiEntry.antenna_sel = csi_dict["antenna_sel"]
        csiEntry.length = csi_dict["length"]
        csiEntry.rate = csi_dict["rate"]
        csiEntry.rssiA_db = csi_dict["rssiA_db"]
        csiEntry.rssiB_db = csi_dict["rssiB_db"]
        csiEntry.rssiC_db = csi_dict["rssiC_db"]



        csiEntry.csi = csi_dict["csi"]
        csiEntry.perm = csi_dict["perm"]
        csiEntry.csi_pwr = csi_dict["csi_pwr"]
        csiEntry.rssi_pwr = csi_dict["rssi_pwr"]
        csiEntry.rssi_pwr_db = csi_dict["rssi_pwr_db"]
        csiEntry.scale = csi_dict["scale"]
        csiEntry.noise_db = csi_dict["noise_db"]
        csiEntry.quant_error_pwr = csi_dict["quant_error_pwr"]
        csiEntry.total_noise_pwr =  csi_dict["total_noise_pwr"]
        csi_list = csiEntry.csi
        for rx in range(len(csi_list)):
            for tx in range(len(csi_list[rx])):
                for i in range(len(csi_list[rx][tx])):
                    csi_list[rx][tx][i] = complex(csi_list[rx][tx][i])
        csiEntry.csi = csi_list
        return csiEntry
    def __str__(self):
        myString = "CSI Entry:\n"
        myString += "\t Correct: " + str(self.correct) + "\n"
        if not self.correct:
            return myString

        myString += "\t Code: " + str(self.code) + "\n"
        myString += "\t bfee_count: " + str(self.bfee_count) + "\n"
        myString += "\t Ntx: " + str(self.Ntx) + "\n"
        myString += "\t Nrx: " + str(self.Nrx) + "\n"
        myString += "\t MCS Rate: " + str(self.rate) + "\n"
        myString += "\t Rssi A [dB]: " + str(self.rssiA_db) + "\n"
        myString += "\t Rssi B [dB]: " + str(self.rssiB_db) + "\n"
        myString += "\t Rssi C [dB]: " + str(self.rssiC_db) + "\n"
        myString += "\t Total Rssi [dB]: " + str(np.round(self.rssi_pwr_db,2)) + "\n"
        myString += "\t Agc: " + str(self.agc) + "\n"
        myString += "\t Antenna Sel: " + str(self.antenna_sel) + "\n"
        myString += "\t Thermal Noise [dB]: " + str(self.noise_db) + "\n"
        myString += "\t Quantization Noise [dB]: " + str(np.round(self.quant_error_pwr,2)) + "\n"
        myString += "\t Total Noise [dB]: " + str(np.round(self.total_noise_pwr,2)) + "\n"
        myString += "\t Permutation vector: " + str(self.perm) + "\n"
        myString += "\t CSI matrix: " + str(self.csi) + "\n"
        return myString

    def _to_json(self):
        def default(prop):
            if "numpy" in  str(type(prop)):
                print(f"prop is numpy :tpye {type(prop)} prop ->{prop}")
                return prop.tolist()
            if "__dict__" in dir(prop):
                print("has prop")
                return prop.__dict__
            else:
                print(f"Prop has no __dict__ {type(prop)}: \n {prop}")
                #return prop
        json_str = ""
        csi_save = self.csi.copy()

        csi_list = self.csi.tolist()

        for rx in range(len(csi_list)):
            for tx in range(len(csi_list[rx])):
                for i in range(len(csi_list[rx][tx])):
                    csi =csi_list[rx][tx][i]
                    csi_list[rx][tx][i] = str(csi)
        self.csi = csi_list
        json_str = json.dumps(self,default=default, indent=True)
        #json_str= json.dumps(self, default=lambda o: o.__dict__, 
        #    sort_keys=True, indent=4)
        self.csi = csi_save
        #json_str= (json.dumps(csi_list))
        return json_str
    
    def to_dict(self):
        return json.loads(self._to_json())
    

def plot_ampli(csi_entry : CsiEntry):
    for tx in range(csi_entry.Ntx):
        for rx in range(csi_entry.Nrx): 
            amplitudes = [abs(csi_comp) for csi_comp in csi_entry.csi[tx][rx]]
            plt.plot(range(len(csi_entry.csi[tx][rx])), amplitudes, label="Antenna {}->{}".format(tx,rx))
        break
    plt.xlabel('Subcarrier index')
    plt.ylabel('amplitude')