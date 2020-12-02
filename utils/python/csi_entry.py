import json
class CsiEntry( json.JSONDecoder):
    """docstring for CsiEntry"""
    def __init__(self):
        super(CsiEntry, self).__init__()
        self.Nrx    = None
        self.Ntx    = None
        self.rss    = None
        self.rssA   = None
        self.rssB   = None
        self.rssC   = None
        self.noise  = None
        self.rss    = None
        self.snr    = None
        self.csi    = []
        self.src_mac                 = None
        self.seq_nr                  = None
        self.spartial_stream_core_nr = None
        self.chanspec                = None
        self.chip_version            = None
        self.csi_matrix              = None
        self.csi_matrix_size         = None

    @classmethod
    def from_dict(cls, csi_dict):
        """
        init from json
        """
        csiEntry                            = cls()
        csiEntry.rx                         = csi_dict.get("rx", None)                    
        csiEntry.rssiA                      = csi_dict.get("rss", None)                   
        csiEntry.rssiA                      = csi_dict.get("rssA", None)                  
        csiEntry.rssiB                      = csi_dict.get("rssB", None)                  
        csiEntry.rssiC                      = csi_dict.get("rssC", None)                      
        csiEntry.noise                      = csi_dict.get("noise", None)                     
        csiEntry.snr                        = csi_dict.get("snr", None)                           
        csiEntry.csi                        = csi_dict.get("csi", None)                           
        csiEntry.src_mac                    = csi_dict.get("src_mac", None)                   
        csiEntry.seq_nr                     = csi_dict.get("seq_nr", None)                        
        csiEntry.spartial_stream_core_nr    = csi_dict.get("spartial_stream_core_nr", None)       
        csiEntry.chanspec                   = csi_dict.get("chanspec", None)                  
        csiEntry.chip_version               = csi_dict.get("chip_version", None)              
        csiEntry.csi_matrix                 = csi_dict.get("csi_matrix", None)                
        csiEntry.csi_matrix_size            = csi_dict.get("csi_matrix_size", None)           
        return csiEntry


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


        for i in range(len(csi_list)):
            csi =csi_list[i]
            csi_list[i] = str(csi)
        self.csi = csi_list
        json_str = json.dumps(self,default=default, indent=True)
        self.csi = csi_save
        return json_str
    
    def to_dict(self):
        return json.loads(self._to_json())
    