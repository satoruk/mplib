from app.gram_scale import GramScale
from lcd.hd44780.simple import HD44780
from load_cell.hx711.simple import HX711
from machine import Pin
import sys
import time

def main():
  lcd = HD44780(
    rs=21,
    en=20,
    d4=19,
    d5=18,
    d6=17,
    d7=16,
  )
  lcd.init()
  lcd.string("     ", HD44780.LINE1)
  lcd.string("HELLO", HD44780.LINE2)

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

    # 有効数字8桁で表示
    line1 = "value: {0:7.3f} g".format(value)
    print(line1)
    lcd.string(line1, HD44780.LINE2)
    time.sleep_ms(100)


if __name__ == '__main__':
  print(sys.version)
  print("Starting")
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print("Goodbye!")
        