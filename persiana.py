from btle import UUID, Peripheral, BTLEException
import struct
import math
import pexpect
#class KeypressSensor(SensorBase):
# TODO: only sends notifications, you can't poll it
#    svcUUID = UUID(0xFFE0)
# write 0100 to 0x60
# get notifications on 5F

class SensorTag(Peripheral):
    def __init__(self,addr):
        Peripheral.__init__(self,addr)
        self.discoverServices()

if __name__ == "__main__":
    import time

    #tag = SensorTag("BC:6A:29:AB:D3:7A")
    
    resp=pexpect.spawn('hciconfig hci0 up')
    resp.expect('.*')
    Debugging = False
    #devaddr = sys.argv[1] + " random"
    devaddr = "de:2d:06:53:4b:ad random"
    print("Connecting to:", devaddr)
    a='s'
    while a=='s':
        try:
            conn = Peripheral(devaddr)
            while True:
                n = input("Ponga (s) para salir:")
                cmd='00:00'
                if n.strip() == '1':
                    cmd='01:00'
                if n.strip() == '2':
                    cmd='02:00'
                try:
                    conn.writeCharacteristic(14,cmd)
                except BTLEException as e:
                    print ("write error:")
                    print (e)
                    print ("Try again? (s/n)")
                    b=input()
                    if b == 's':
                        a='s'
                        break
                else:
                    b='n'
                if n.strip() == 's':
                    a='n'
                    break
        except BTLEException as e:
            print ("ERROR!!!!")
            print (e)
            print ("desea intentarlo de nuevo (s/n)?")
            a=input()
        finally:
            print ("saliendo")
            #conn.disconnect()
