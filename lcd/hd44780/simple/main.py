from HD44780 import HD44780

def main():
  print("foo")
  lcd = HD44780(
    rs=21,
    en=20,
    d4=19,
    d5=18,
    d6=17,
    d7=16,
  )
  lcd.init()
  lcd.string("abc", HD44780.LINE1)
  lcd.string("ABC", HD44780.LINE2)

if __name__ == '__main__':
  print("Starting")
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print("Goodbye!")
        