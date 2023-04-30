from lcd.hd44780 import HD44780
from loadcell.hx711 import HX711, mean
import sys



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


  loadcell = HX711(
    pd_sck=14,
    dout=15,
    rate=0.000541
  )
  loadcell.reset()
  loadcell.tare()
  q = []
  while True:
    value = loadcell.measure()
    q.append(value)
    if len(q) > 5:
      q.pop(0)

    adjusted_value = mean(q)

    # 有効数字8桁で表示
    line1 = "value: {0:7.3f} g".format(adjusted_value)
    print(line1)
    lcd.string(line1, HD44780.LINE2)


if __name__ == '__main__':
  print(sys.version)
  print("Starting")
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print("Goodbye!")
        