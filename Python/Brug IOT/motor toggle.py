#  Raspberry Pi Master voor Arduino Slave

from smbus2 import SMBus

addr = 0x0  # arduino bus address (hexadecimaal)
bus = SMBus(1)  # gebruikt /dev/ic2-1 want /dev/ic2-0 is voorbehouden voor pi-hats ("shields" voor op de pi)

def activate_motor():
        bus.write_byte(addr, 0x1)  # schrijf 0x1 (hexadecimal naar arduino), geeft on state
        return
def disalbe_moter():
        bus.write_byte(addr, 0x1) # schrijf 0x0 (hexadecimaal naar arduino), geeft een off state

# schrijft van 0 tot 6 (niet op efficiënte manier is gwn voor test als I2C werkt)
bus.write_byte(addr, 0x0)
bus.write_byte(addr, 0x1)
bus.write_byte(addr, 0x2)
bus.write_byte(addr, 0x3)
bus.write_byte(addr, 0x4)
bus.write_byte(addr, 0x5)
bus.write_byte(addr, 0x6)