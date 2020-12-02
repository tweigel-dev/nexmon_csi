import json
import numpy as np


# DTYPE_UDP = np.dtype([
#     ("port_src", np.bytes[2]),
#     ("port_dst", np.bytes[2]),
#     ("length", np.bytes[2]),   
#     ("checksum", np.bytes[2]), # should be empty
#     ("magic_nexmon", np.bytes[4]),
# ])

# DTYPE_IP_PKT = np.dtype([
#     ("ip_flags", np.bytes[12]),
#     ("adr_ip_src", np.bytes[6]), # should be 10.10.10.10     -> 0x0a0a0a0a
#     ("adr_ip_dst", np.bytes[6]), # should be 255.255.255.255 -> 0xffffffff
#     ("udp_pkt",DTYPE_UDP)
# ])


DTYPE_FRAME = np.dtype([
    ("adr_destination_broadcast", np.array(4,dtype=np.dtype('b'))),
    ("adr_source_nexmon", np.array(4,dtype=np.dtype('b'))),
    ("ip_type", np.dtype('i4')) # 0x0800 -> IPv4
  #  ("ip_pkt", DTYPE_IP_PKT),
])

# myMac_intel = "00:21:6a:ba:7f:a0" # dell intel5300
# DTYPE_CSI_HEADER_TLV = np.dtype([
#     ("code", np.bytes[6]),
#     ("timestamp_low", np.uint32),
#     ("bfee_count", np.uint16),
#     ("reserved1", np.uint16),
#     ("Nrx", np.uint8),
#     ("Ntx", np.uint8),
#     ("rssiA", np.uint8),
#     ("rssiB", np.uint8),
#     ("rssiC", np.uint8),
#     ("noise", np.int8),
#     ("agc", np.uint8),
#     ("antenna_sel", np.uint8),
#     ("len", np.uint16),
#     ("fake_rate_n_flags", np.uint16),
# ]).newbyteorder('<')


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