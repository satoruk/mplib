from machine import Pin
from time import sleep, sleep_ms, sleep_us
import sys

def mean(data):
    if iter(data) is data:
        data = list(data)
    return sum(data)/len(data)

class HX711(object):
  CHR = True

  def __init__(self, dout, pd_sck, gain=128):
    print("HX711.__init__")
    print({
      'dout': dout,
      'pd_sck': pd_sck,
    })
    self.dout = Pin(dout, Pin.IN)
    self.pd_sck = Pin(pd_sck, Pin.OUT)
    self.base = 0
    # キャリブレーション
    # 期待する重さ(g) / 実際に計測された値
    self.rate = 0.0004953425

  def read(self):
    sleep_ms(300)
    # 24 bits of data
    raw = 0
    for i in range(24):
      self.pd_sck.value(True)
      sleep_us(1)
      self.pd_sck.value(False)
      sleep_us(1)
      raw = (raw << 1) | (self.dout.value())

    if raw & 0x800000 == 0x800000:
      raw = -(raw ^ 0x800000)

    return raw

  def tare(self, times=10):
    q = []
    for i in range(times):
      value = self.read()
      q.append(value)

    self.base = mean(q)

  def measure(self):
    value = self.read()
    value = value - self.base
    return value * self.rate

if __name__ == '__main__':
  print(sys.version)
  print("Starting")
  try:
    loadcell = HX711(pd_sck=14, dout=15)
    loadcell.tare()
    while True:
      print(f" weight:{loadcell.measure()}")

  except KeyboardInterrupt:
    pass
  finally:
    print("Goodbye!")
        
