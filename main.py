from lcd.hd44780 import HD44780
# import lcd

def main():
  print("Setup")
  HD44780()


if __name__ == '__main__':
  print("Starting2")
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    print("Goodbye!")
        
