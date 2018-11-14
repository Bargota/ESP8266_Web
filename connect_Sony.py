import network 
import time
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
nets = wlan.scan()
for net in nets:
    if net[0] == b'Xperia XZ1 Compact_8fc6':
        print('Network found!')
        wlan.connect('Xperia XZ1 Compact_8fc6','12345678')
        
        print(str(net[0]))
        print(str(net[1]))
        #while not wlan.isconnected():
            #print('WLAN not connection')
            #pass
            #machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        time.sleep(1)
        print(wlan.ifconfig())
        break
