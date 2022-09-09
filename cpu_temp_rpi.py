import sys
import os
from time import sleep
from gpiozero import CPUTemperature
import urllib.request as urllib2

myAPI = "0WDRHQ0MYH14VFGD"
myDelay = 15

def main():
    print('starting..')
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    print(baseURL)
    
    while True:
        try:
            cpu = CPUTemperature()
            f = urllib2.urlopen(baseURL +"&field1=%s" % (cpu.temperature))
            print(f.read())
            f.close()
            sleep(int(myDelay))
        except:
            print('exiting')
            break
if __name__ == "__main__":
    main()
               

