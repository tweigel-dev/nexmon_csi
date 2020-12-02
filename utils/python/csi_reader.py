BANDWIDTH ={ # MHz to size of CSI
    "20": 64,
    "40": 128,
    "80": 256
}
import matplotlib.pyplot as plt
FRAME_IP_HEADER_SIZE = 42
UDP_HEADER_SIZE = 18 # bytes without csi flow
from pylibpcap.pcap import rpcap as cap
import numpy as np
import json
import csi_plot as plot

#FILE = "./example.pcap"
FILE = "capture_output_bcm43455c0.pcap"
import os
#import CsiEntry
CHIPS = ["bcm43455c0"]
def extract_csi(udp_payload):

    def format_csi(csi_hex, chip):
        if len(csi_hex) % 8 != 0:
            raise Exception(f"size if csi is wrong:{len(csi_hex)}\n should be devideable by 8")
        if not chip in CHIPS :
            raise Exception("chip is not supported")
        csi_values = []
        csi_cnt =int(len(csi_hex)/8)
        for step in range(csi_cnt):
            offset = step*8
            
            comp_csi = complex(int(csi_hex[offset:offset+4].hex(),16),int(csi_hex[offset+5:offset+8].hex(), 16))
            csi_values.append(comp_csi)
        return csi_values


    udp_dict ={}
    udp_dict["src_mac"]                 = udp_payload[4:10].hex()
    udp_dict["seq_nr"]                  = udp_payload[10:11].hex()
    udp_dict["spartial_stream_core_nr"] = udp_payload[12:13].hex()
    udp_dict["rx"]                      = 1 # TODO merge multible packages
    udp_dict["chanspec"]                = udp_payload[14:15].hex()
    udp_dict["chip_version"]            = udp_payload[16:17].hex()
    print(udp_dict)
    udp_dict["csi"]              = format_csi(udp_payload[UDP_HEADER_SIZE:],CHIPS[0]) 
    udp_dict["csi_matrix_size"]         = len(udp_dict["csi"])

    entry = plot.CsiEntry.from_dict(udp_dict)
    return entry
if __name__ == "__main__":
    if not os.path.isfile(FILE):
        raise Exception(f"No file found {FILE}")

    p = cap(FILE)
    csi_entrys = []

    for length, t, pkt in p:
        print(f"size of frame:{length}")
        udp_payload = pkt[FRAME_IP_HEADER_SIZE:]
        #print(udp_payload)
        payload_len = len(udp_payload)
        if payload_len == (UDP_HEADER_SIZE + 4*BANDWIDTH["20"]):
            pass
        elif payload_len == (UDP_HEADER_SIZE + 4*BANDWIDTH["40"]):
            pass
        elif payload_len == (UDP_HEADER_SIZE + 4*BANDWIDTH["80"]):
            pass
        else:
            print("scipped pacakges")
            continue
            #raise Exception(f"invalid udp_payload length :{payload_len}")
        csi_entry = extract_csi(udp_payload)
        csi_entrys.append(csi_entry)

    plt.subplot()
    for entry in csi_entrys[:10]:
        plot.plot_ampli(entry) 
    plt.show()










# CHIP = '4358'            # wifi chip (possible values 4339, 4358, 43455c0, 4366c0)
# BW = 80                  # bandwidth
# FILE = './example.pcap'  # capture file
# NPKTS_MAX = 1000         # max number of UDPs to process
# HOFFSET = 16             # header offset
# NFFT = BW*3.2            # fft size
# p = readpcap() 
# p.open(FILE) 

# n = min(length(p.all()),NPKTS_MAX) 
# p.from_start() 
# csi_buff = complex(zeros(n,NFFT),0) 
# k = 1 

# while (k <= n):
#     f = p.next() 
#     if isempty(f):
#         disp('no more frames') 
#         break 
    
#     if f.header.orig_len-(HOFFSET-1)*4 != NFFT*4:
#         disp('skipped frame with incorrect size') 
#         continue 
    
#     payload = f.payload 
#     H = payload(HOFFSET:HOFFSET+NFFT-1) 
#     if (strcmp(CHIP,'4339') or strcmp(CHIP,'43455c0')):
#         Hout = typecast(H, 'int16') 
#     elif (strcmp(CHIP,'4358')):
#         Hout = unpack_float(int32(0), int32(NFFT), H) 
#     elif (strcmp(CHIP,'4366c0')):
#         Hout = unpack_float(int32(1), int32(NFFT), H) 
#     else:
#         disp('invalid CHIP') 
#         break 

#     Hout = reshape(Hout,2,[]).' 
#     cmplx = double(Hout(1:NFFT,1))+1j*double(Hout(1:NFFT,2)) 
#     csi_buff(k,:) = cmplx.' 
#     k = k + 1 


#  # # plot
# plotcsi(csi_buff, NFFT, false)

