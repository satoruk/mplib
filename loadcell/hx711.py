from machine import Pin
from time import sleep, sleep_ms, sleep_us
import sys

def mean(data):
    if iter(data) is data:
        data = list(data)
    return sum(data)/len(data)

class HX711(object):
  CHR = True

  # Channnel A, gain factor 128
  MODE1 = 25

  # Channnel B, gain factor 32
  MODE2 = 26

  # Channnel A, gain factor 64
  MODE3 = 27


  def __init__(self, dout, pd_sck, rate=0.000547):
    print("HX711.__init__")
    print({
      'dout': dout,
      'pd_sck': pd_sck,
    })
    self.dout = Pin(dout, Pin.IN)
    self.pd_sck = Pin(pd_sck, Pin.OUT)
    self.base = 0
    self.rate = rate
    self.mode = self.MODE1

  def select_mode(self, mode = MODE1):
    # 0.1 us < t1
    sleep_us(1)

    for i in range(mode):
      # 0.2 us < t3 < 50 us
      self.pd_sck.value(True)
      sleep_us(1)

      # 0.2 us < t4
      self.pd_sck.value(False)
      sleep_us(1)

  def reset(self):
    """リセット
    リセット以降は
    """
    self.power_down()
    sleep_us(10) # おまけ
    self.power_up()

  def power_down(self):
    """省電力モード
    """
    # 0.1 us < t1
    sleep_us(1)

    self.pd_sck.value(True)
    sleep_us(60)

  def power_up(self):
    """省電力モードからの復帰
    """
    self.pd_sck.value(False)
    self.wait_ready()

  def wait_ready(self):
    i = 0
    while True:
      if self.dout.value() == 0:
        if i > 0:
          print(f"wait_ready: {i * 50} ms")
        break

      sleep_ms(50)
      i = i + 1

  def read(self):
    # 0.1 us < t1
    sleep_ms(300)
    self.wait_ready()
    # 24 bits of data
    raw = 0

    for i in range(24):
      #          t2 <  0.1 us
      # 0.2 us < t3 < 50.0 us
      # 0.3 us < t  < 50.0 us
      self.pd_sck.value(True)
      sleep_us(1)

      raw = (raw << 1) | (self.dout.value())

      # 0.2 us < t4
      self.pd_sck.value(False)
      sleep_us(1)

    if raw & 0x800000 == 0x800000:
      raw = -(raw ^ 0xffffff)

    return raw

  def tare(self, times=10):
    q = []
    for i in range(times):
      value = self.read()
      q.append(value)

    self.base = mean(q)
  
  def calibrate(self, weight, times=10):
    """キャリブレーション
    
    Arguments:
      weight {int} -- 期待する重さ(g)
      times {int} -- 平均を取る回数
    """
    q = []
    for i in range(times):
      value = self.read() - self.base
      q.append(value)
      sleep_ms(300)

    print(f"calibrate: {q}")
    print(f"mean: {mean(q)}")
    self.rate = weight / mean(q)

  def measure(self):
    value = self.read()
    value = value - self.base
    return value * self.rate

if __name__ == '__main__':
  print(sys.version)
  print("Starting")
  try:
    loadcell = HX711(pd_sck=14, dout=15)
    loadcell.reset()
    loadcell.tare()
    base = loadcell.base
    q = [
      0, 0, 0, 0, 0,
      0, 0, 0, 0, 1,
    ]
    sample_waight = 12.22
    sample_waight = 450.09
    rate = 0.000547
    rate = 0.000541
    while True:
      v = loadcell.read()
      q.append(v - base)
      q.pop(0)
      print(
        (
          "read:{read:8} "
          "base:{base:8} "
          "value:{value:8.3f} "
          "rate:{rate:f} "
        ).format(
          read=v,
          base=base,
          value=(v - base) * rate,
          rate= sample_waight / mean(q)
        )
      )

    # loadcell.tare()

    # for i in range(3, 0, -1):
    #   print(f" calibrate count down: {i}")
    #   sleep(5)

    # loadcell.calibrate(weight=0.0)
    # # loadcell.calibrate(weight=464.97)
    # print(f" calibrate done: {loadcell.rate}")
    # sleep(10)

    # while True:
    #   print(f" weight:{loadcell.measure()} rate:{loadcell.rate}")

  except KeyboardInterrupt:
    pass
  finally:
    print("Goodbye!")
        
