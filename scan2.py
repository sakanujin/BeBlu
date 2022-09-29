from bluepy.btle import Scanner, DefaultDelegate
import time

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            pass
            #print("Discovered device", dev.addr)
        elif isNewData:
            #print("Received new data from", dev.addr)
            pass

while True:
 
  scanner = Scanner().withDelegate(ScanDelegate())
  devices = scanner.scan(10.0)

  for dev in devices:
     if (dev.addr == '74:90:50:40:bb:5c'):
         #print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
         for (adtype, desc, value) in dev.getScanData():
             print("  %s = %s" % (desc, value))

