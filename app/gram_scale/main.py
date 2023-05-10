from machine import Pin
from load_cell.hx711.simple import HX711
from GramScale import GramScale
from time import sleep

def main():
  pin_OUT = Pin(15, Pin.IN, pull=Pin.PULL_DOWN)
  pin_SCK = Pin(14, Pin.OUT)
  # 重さ / 値
  rate = 450 / 846423

  hx711 = HX711(pin_SCK, pin_OUT)
  scale = GramScale(load_cell=hx711, rate=rate, buff_size=10)

  print("tare")
  scale.tare()
  print("tare ... done")

  while True:
    value = scale.value()
    print(f"value: {value:7.3f} g")
    sleep(0.5)

if __name__ == '__main__':
  print("Starting")
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print("Goodbye!")
 