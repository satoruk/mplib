from lcd.hd44780 import HD44780
from loadcell.hx711 import HX711
import sys



def main():
  lcd = HD44780(
    rs=26,
    en=22,
    d4=21,
    d5=20,
    d6=19,
    d7=18,
  )
  lcd.init()
  lcd.string("     ", HD44780.LINE1)
  lcd.string("HELLO", HD44780.LINE2)


  # loadcell = HX711(pd_sck=14, dout=15)
  # loadcell.tare()
  # while True:
  #   value = loadcell.measure()

  #   # 有効数字8桁で表示
  #   line1 = "value: {0:8.3f} g".format(value)
  #   print(line1)
  #   lcd.string(line1, HD44780.LINE2)


if __name__ == '__main__':
  print(sys.version)
  print("Starting")
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print("Goodbye!")
        