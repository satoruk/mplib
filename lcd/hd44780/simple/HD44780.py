from machine import Pin
from time import sleep_us

class HD44780(object):
  CHR = True
  CMD = False
  LINE1 = 0x80  # LCD RAM address for the 1st line
  LINE2 = 0xC0  # LCD RAM address for the 2nd line
  EN_PULSE = 500
  EN_DELAY = 500

  def __init__(self, rs, en, d4, d5, d6, d7, col=16, row=2):
    # print("HD44780.__init__2")
    # print({
    #   'rs': rs,
    #   'en': en,
    #   'd4': d4,
    #   'd5': d5,
    #   'd6': d6,
    #   'd7': d7,
    #   'col': col,
    #   'row': row
    # })

    self.rs = Pin(rs, Pin.OUT)
    self.en = Pin(en, Pin.OUT)
    self.d4 = Pin(d4, Pin.OUT)
    self.d5 = Pin(d5, Pin.OUT)
    self.d6 = Pin(d6, Pin.OUT)
    self.d7 = Pin(d7, Pin.OUT)
    self.col = col
    self.row = row

  def toggle_enable(self):
    # Toggle enable
    sleep_us(self.EN_DELAY)
    self.en.value(1)
    sleep_us(self.EN_PULSE)
    self.en.value(0)
    sleep_us(self.EN_DELAY)

  def byte(self, bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command

    self.rs.value(mode)  # RS

    # High bits
    self.d4.value(bool(bits & 0x10))
    self.d5.value(bool(bits & 0x20))
    self.d6.value(bool(bits & 0x40))
    self.d7.value(bool(bits & 0x80))

    # Toggle 'Enable' pin
    self.toggle_enable()

    # Low bits
    self.d4.value(bool(bits & 0x01))
    self.d5.value(bool(bits & 0x02))
    self.d6.value(bool(bits & 0x04))
    self.d7.value(bool(bits & 0x08))

    # Toggle 'Enable' pin
    self.toggle_enable()
    # print(
    #   # '| {rs} | {en} | {d07}{d06}{d05}{d04}_{d17}{d16}{d15}{d14}'.format(
    #   '| {rs} | {en} | 00{d05}{d04}_00{d15}{d14}'.format(
    #     rs=int(mode),
    #     en=1,
    #     d04=int(bool(bits & 0x10)),
    #     d05=int(bool(bits & 0x20)),
    #     d06=int(bool(bits & 0x30)),
    #     d07=int(bool(bits & 0x40)),
    #     d14=int(bool(bits & 0x01)),
    #     d15=int(bool(bits & 0x02)),
    #     d16=int(bool(bits & 0x04)),
    #     d17=int(bool(bits & 0x08)),
    #   )
    # )

  def init(self):
    # Initialise display
    self.byte(0x33, self.CMD)  # 0x33 110011 Initialise
    self.byte(0x32, self.CMD)  # 0x32 110010 Initialise
    self.byte(0x06, self.CMD)  # 0x06 000110 Cursor move direction
    self.byte(0x0C, self.CMD)  # 0x0C 001100 Display On,Cursor Off, Blink Off
    self.byte(0x28, self.CMD)  # 0x28 101000 Data length, number of lines, font size
    self.byte(0x01, self.CMD)  # 0x01 000001 Clear display
    sleep_us(self.EN_DELAY)

  def string(self, message, line):
    # Send string to display
    message = message + " " * (self.col - len(message))
    print("lcd_string(" + message + ")")

    self.byte(line, self.CMD)

    for i in range(self.col):
        self.byte(ord(message[i]), self.CHR)
