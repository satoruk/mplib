import machine
import utime

# https://www.youtube.com/watch?v=hW-1WWTrvCo

lcd_RS = machine.Pin(16, machine.Pin.OUT)

lcd_E = machine.Pin(17, machine.Pin.OUT)
lcd_D4 = machine.Pin(18, machine.Pin.OUT)
lcd_D5 = machine.Pin(19, machine.Pin.OUT)
lcd_D6 = machine.Pin(20, machine.Pin.OUT)
lcd_D7 = machine.Pin(21, machine.Pin.OUT)

def lcd_ini():
    lcd_RS.value(0)
    utime.sleep(0.04)
    lcd_send(0b0011)
    lcd_send(0b0011)
    lcd_send(0b0011)
    lcd_send(0b0010)

    lcd_send(0b0010)
    lcd_send(0b1000)

    lcd_send(0b0000)
    lcd_send(0b1100)

    lcd_send(0b0000)
    lcd_send(0b0001)

    lcd_send(0b0000)
    lcd_send(0b0110)
    utime.sleep(0.2)

def lcd_wait():
    lcd_E.value(1)
    utime.sleep_us(40)
    lcd_E.value(0)
    utime.sleep_us(40)

def lcd_clr():
    lcd_RS.value(0)
    lcd_send(0b0000)
    lcd_send(0b0001)
    utime.sleep(0.01)
    lcd_RS.value(1)

def lcd_send(Bindata):
    lcd_D4.value((Bindata & 0b0001) >>0)
    lcd_D5.value((Bindata & 0b0010) >>1)
    lcd_D6.value((Bindata & 0b0100) >>2)
    lcd_D7.value((Bindata & 0b1000) >>3)
    lcd_wait()

def lcd_str(strdata):
    for x in strdata:
        lcd_send(ord(x) >> 4)
        lcd_send(ord(x) >> 0)

lcd_ini()
lcd_RS.value(1)

while True:
    lcd_clr()
    lcd_str("Hello World")
    utime.sleep(1)
    lcd_clr()
    lcd_str("Raspberry Pi")
    utime.sleep(1)