#
#{'type': 'result', 'timestamp': '2021-07-28T20:18:12Z', 'ping': {'jitter': 113.391, 'latency': 11.021}, 'download': {'bandwidth': 6585205, 'bytes': 26736784, 'elapsed': 4011}, 
# 'upload': {'bandwidth': 335749, 'bytes': 4145624, 'elapsed': 13002}, 'packetLoss': 0, 'isp': 'Comcast Cable', 'interface': {'internalIp': '172.26.20.19', 'name': 'eth0', 'macAddr': '00:15:5D:14:AA:7B', 
# 'isVpn': False, 'externalIp': '71.201.6.178'}, 'server': {'id': 12187, 'name': 'Nitel', 'location': 'Chicago, IL', 'country': 'United States', 'host': 'speedtest.chi1.nitelusa.net', 
# 'port': 8080, 'ip': '45.61.24.34'}, 'result': {'id': '9f30b31a-a43d-4c6a-a6f6-8f09356b0a84', 'url': 'https://www.speedtest.net/result/c/9f30b31a-a43d-4c6a-a6f6-8f09356b0a84'}}
#dowloadspeed = 6.665864871603091 mbps


import os
import subprocess
import json
import math
import numpy as np
import threading
import time

#wifispeed = subprocess.run(["speedtest", "--format=json"], stdout=subprocess.DEVNULL)
from subprocess import check_output


def CheckInternetSpeed():
    count = 0
    while 1:
        count +=1
        print (" TEST # " + str(count))
        out = check_output(["speedtest", "--format=json"])
        out = json.loads(out)

        print ("result:  ")
        print (out)
        #downloadspeed = int(wifispeed['download']['bytes'])/int(wifispeed['download']['elapsed'])
        dbytes= int(out['download']['bytes'])*8
        elapsed = int(out['download']['elapsed'])
        download_speed = np.round(float(dbytes/elapsed/1000), 2)



        ubytes= int(out['upload']['bytes'])*8
        elapsed = int(out['upload']['elapsed'])
        upload_speed = np.round(float(ubytes/elapsed/1000), 2)
        jitter = np.round(float(out['ping']['jitter']))
        latency = np.round(float(out['ping']['latency']))
        pkt_loss = np.round(float(out['packetLoss']))
        print("timesampe  = " + str(download_speed) + " mbps")
        print("jitter = " + str(upload_speed) + " ms")
        print("latency = " + str(download_speed) + " ms")
        print("dowload speed = " + str(download_speed) + " mbps")
        print("upload speed = " + str(upload_speed) + " mbps")

        file2 = open("wifilog.txt", "a")

        # ["datetime", "isp", "download", "upload", "jitter", "latency", "location"]
        str1 = str(out['timestamp'])+","+out['isp']+","+str(download_speed)+","+str(upload_speed)+","+str(jitter)+","+str(latency)+","+str(pkt_loss)+","+out['server']['location']+"\n"
        file2.write (str1)
        file2.close()    
        time.sleep(60*10)

if __name__ == '__main__':
    thread1 = threading.Thread(target = CheckInternetSpeed)
    thread1.start()


